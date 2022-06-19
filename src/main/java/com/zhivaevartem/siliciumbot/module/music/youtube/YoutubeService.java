package com.zhivaevartem.siliciumbot.module.music.youtube;

import com.zhivaevartem.siliciumbot.util.StringUtils;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.http.ResponseEntity;
import org.springframework.stereotype.Service;
import org.springframework.web.client.RestTemplate;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Map;

@Service
public class YoutubeService {
  @Value("${silicium.youtube-token}")
  private String youtubeApiKey;

  private final String YOUTUBE_SEARCH_API
    = "https://www.googleapis.com/youtube/v3/search?part=id&maxResults={limit}&type=video&q={query}&key={key}";
  private final String YOUTUBE_PLAYLIST_ITEMS_API
    = "https://www.googleapis.com/youtube/v3/playlistItems?key={key}&part=contentDetails&playlistId={id}&maxResults={limit}";

  public List<String> searchVideos(String query) {
    return this.searchVideos(query, 1);
  }

  public List<String> searchVideos(String query, int limit) {
    RestTemplate restTemplate = new RestTemplate();
    String url = this.YOUTUBE_SEARCH_API
      .replace("{query}", query)
      .replace("{key}", this.youtubeApiKey)
      .replace("{limit}", Integer.toString(limit));
    ResponseEntity<YoutubeSearchResponse> response = restTemplate.getForEntity(url, YoutubeSearchResponse.class);
    YoutubeSearchResponse body = response.getBody();
    if (body != null && body.getItems() != null) {
      return Arrays.stream(body.getItems()).map(item -> item.getId().getVideoId()).toList();
    }
    return new ArrayList<>(0);
  }

  public List<String> getPlaylistVideos(String url) {
    return this.getPlaylistVideos(url, 50);
  }

  public List<String> getPlaylistVideos(String url, int limit) {
    RestTemplate restTemplate = new RestTemplate();
    String playListId = this.getPlaylistIdFromUrl(url);
    String apiUrl = this.YOUTUBE_PLAYLIST_ITEMS_API
      .replace("{key}", this.youtubeApiKey)
      .replace("{limit}", Integer.toString(limit))
      .replace("{id}", playListId);
    ResponseEntity<YoutubePlaylistItemsResponse> response
      = restTemplate.getForEntity(apiUrl, YoutubePlaylistItemsResponse.class);
    YoutubePlaylistItemsResponse body = response.getBody();
    if (body != null && body.getItems() != null) {
      return Arrays.stream(body.getItems()).map(item -> item.getContentDetails().getVideoId()).toList();
    }
    return new ArrayList<>(0);
  }

  private String getPlaylistIdFromUrl(String url) {
    Map<String, String> params = StringUtils.parseQueryParams(url);
    if (params.containsKey("list")) {
      return params.get("list");
    }
    return "";
  }
}
