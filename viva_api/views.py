import requests
from django.http import JsonResponse


def stories(request):
    index = int(request.GET.get("index"))
    max_number = int(request.GET.get("max_number"))
    stories_data = []

    top_stories_url = "https://hacker-news.firebaseio.com/v0/topstories.json"
    top_stories_data = requests.get(top_stories_url).json()

    for story_id in top_stories_data[index:max_number]:
        story_detail_url = f"https://hacker-news.firebaseio.com/v0/item/{story_id}.json"
        story_detail_data = requests.get(story_detail_url).json()

        stories_data.append(
            {
                "id": story_detail_data["id"],
                "title": story_detail_data["title"],
                "score": story_detail_data["score"],
                "type": story_detail_data["type"],
                "url": story_detail_data["url"],        
            }
        )
    return JsonResponse({"stories_data": stories_data})
