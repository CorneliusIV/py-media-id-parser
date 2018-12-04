import pytest
import media_id_parser

def test_youtube():
    youtube_url = 'https://www.youtube.com/watch?v=T-TwcmT6Rcw'
    video_id = media_id_parser.parse_youtube(youtube_url)
    assert video_id == 'T-TwcmT6Rcw'

def test_twitter():
    twitter_url = 'https://twitter.com/ThePSF'
    twitter_id = media_id_parser.parse_twitter(twitter_url)
    assert twitter_id == 'ThePSF'

def test_spotify():
    spotify_url = 'https://open.spotify.com/track/2NTDt9Fiqp5wTBM6cLO6Bu?si=Vo_97Ri9R8qBAhG_XDbZyg'
    song_id = media_id_parser.parse_spotify(spotify_url)
    assert song_id == '2NTDt9Fiqp5wTBM6cLO6Bu'

def test_instagram():
    instagram_url = 'https://www.instagram.com/p/Bpfqb8ahoKp/'
    post_id = media_id_parser.parse_instagram(instagram_url)
    assert post_id == 'Bpfqb8ahoKp'

def test_vimeo():
    video_url = 'https://vimeo.com/27976435'
    video_id = media_id_parser.parse_vimeo(video_url)
    assert video_id == '27976435'

def test_facebook():
    facebook_url = 'https://www.facebook.com/ESPN/posts/2415420581838017'
    facebook_id = media_id_parser.parse_facebook(facebook_url)
    assert facebook_id == '104266592953439_2415420581838017'