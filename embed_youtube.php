
<?php


// API config 
$API_Key    = 'AIzaSyCJQOUp0LBSGIiw3RN5kotYiZW5PH23rSU'; 
$Channel_ID = 'UCeeKrGQ8TBgE3Vb3UmcPeRg'; 
$Max_Results = 10; 
 
// Get videos from channel by YouTube Data API 
$apiData = file_get_contents('https://www.googleapis.com/youtube/v3/playlists?part=snippet&channelId='.$Channel_ID.'&maxResults&key='.$API_Key.''); 
var_dump($apiData);
if($apiData){ 
    $videoList = json_decode($apiData); 
}else{ 
    echo 'Invalid API key or channel ID.'; 
}


?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>

<?php 

if(!empty($videoList->items)){ 
    foreach($videoList->items as $item){ 
        // Embed video 
        if(isset($item->id->videoId)){ 
            echo ' 
            <div class="yvideo-box"> 
                <iframe width="280" height="150" src="https://www.youtube.com/embed/'.$item->id->videoId.'" frameborder="0" allowfullscreen></iframe> 
                <h4>'. $item->snippet->title .'</h4> 
            </div>'; 
        } 
    } 
}else{ 
    echo '<p class="error">'.$apiError.'</p>'; 
}

?>
    
    
</body>
</html>