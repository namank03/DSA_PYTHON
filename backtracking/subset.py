from pprint import pprint

test_inp = (
    [
        {
            "url": "video1",
            "duration": 10,
            "hashtags": [
                "#travelling",
                "#international",
                "#airport",
                "#coffee",
                "#firstTrip",
                "#1up",
            ],
        },
        {
            "url": "video2",
            "duration": 10,
            "hashtags": ["#moonWalk", "#dance", "#nyc", "#nightlife"],
        },
        {
            "url": "video3",
            "duration": 10,
            "hashtags": ["#icecream", "#cone", "#stick", "#cup"],
        },
        {"url": "video4", "duration": 5, "hashtags": ["#swimming", "#workout"]},
        {
            "url": "video5",
            "duration": 10,
            "hashtags": ["#summer", "#iphone11", "#stick", "#beach"],
        },
        {"url": "video6", "duration": 5, "hashtags": ["#bread", "#cheese"]},
        {"url": "video7", "duration": 5, "hashtags": ["#bread", "#natural", "#fresh"]},
        {
            "url": "video8",
            "duration": 10,
            "hashtags": ["#vanilla", "#fresh", "#icecream", "#summer", "#iphone11"],
        },
        {
            "url": "video9",
            "duration": 10,
            "hashtags": [
                "#banana",
                "#indonesia",
                "#cake",
                "#baking",
                "#rain",
                "#waterfall",
                "#rainForest",
                "#humid",
                "#clouds",
                "#greenLife",
            ],
        },
        {"url": "video10", "duration": 5, "hashtags": ["#fresh", "#natural", "#bread"]},
    ],
)


v = [
    {
        'url': "url1",
        'hashtags': ['#icecream', '#cone', '#stick', '#cup'],
        'duration': 10,
    },
    {
        'url': "url2",
        'hashtags': ['#bread', '#natural', '#fresh', '#cheese'],
        'duration': 10,
    },
    {'url': "url3", 'hashtags': ['#vanilla', '#fresh', '#icecream'], 'duration': 10},
]

# When we've only 10sec videos.
def calculate_score(video1, video2):
    # get hashtags
    hashtags1 = set(video1.get('hashtags', []))
    hashtags2 = set(video2.get('hashtags', []))
    intersection_score = len(hashtags1.intersection(hashtags2))
    video1_score = len(hashtags1 - hashtags2)
    video2_score = len(hashtags2 - hashtags1)
    return min(intersection_score, video1_score, video2_score)


def backtrack(result_list, temp_list, video_list, score, memo):
    # Add condition here to validate the state before adding it to the result list
    # if len(video_list) == 0
    result_list.append((temp_list[:], score))
    if len(temp_list) > 1 and score == 0:
        return

    for i in range(len(video_list)):
        temp_score = 0
        if len(temp_list[:]) > 0:
            # check if the engaing score is avaialble in the memo?
            id1 = video_list[i].get('url')
            id2 = temp_list[-1].get('url')

            if f'{id1}{id2}' in memo:
                temp_score = memo[f'{id1}{id2}']
            elif f'{id2}{id1}' in memo:
                temp_score = memo[f'{id2}{id1}']
            else:
                temp_score = calculate_score(video_list[i], temp_list[:][-1])
            # save the score in memo
            memo[f'{id1}{id2}'] = temp_score

        temp_list.append(video_list[i])
        if temp_score > score:
            backtrack(
                result_list,
                temp_list,
                video_list[:i] + video_list[i + 1 :],
                score + temp_score,
                memo,
            )
        temp_list.pop()


def main_func(video_list):
    memo = {}
    result_list = []
    for i in video_list:
        backtrack(result_list, [i], video_list, 0, memo)

    result_list = sorted(result_list, key=lambda x: (-x[1], len(x[0])))
    return [video.get('url') for video in result_list[0][0]]


# When we've only 10sec & 5sec videos.
v2 = [
    {
        'url': "url1",
        'hashtags': ['#icecream', '#cone', '#stick', '#cup'],
        'duration': 10,
    },
    {'url': "url2", 'hashtags': ['#bread', '#natural', '#fresh'], 'duration': 5},
    {'url': "url4", 'hashtags': ['#bread', '#cheese'], 'duration': 5},
    {'url': "url3", 'hashtags': ['#vanilla', '#fresh', '#icecream'], 'duration': 10},
]

from itertools import combinations, permutations

# 1 way -> filter out the small videos & make all possible permutations & then use the same logic


def combine_short_videos(video1, video2):
    new_video = {'url': video1.get('url') + video2.get('url')}
    new_video['hashtags'] = set(video1.get('hashtags')).union(
        set(video2.get('hashtags'))
    )
    new_video['duration'] = video1.get('duration') + video2.get('duration')
    return new_video


def filter_small_video(video_list, dur=5):
    return [video for video in video_list if video.get('duration') == dur], [
        video for video in video_list if video.get('duration') != dur
    ]


short_videos, long_videos = filter_small_video(test_inp[0])

# res = main_func(long_videos)
# pprint(res)

for video1, video2 in combinations(short_videos, 2):
    long_videos.append(combine_short_videos(video1, video2))


# Now use the same function
res = main_func(long_videos)
pprint(res)
