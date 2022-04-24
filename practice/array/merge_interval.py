# list of videos

from copy import deepcopy

v = [
    {'url': "url1", 'hashtags': ['#tag1', '#tag2', '#tag3', '#tag4'], 'duration': 10},
    {'url': "url2", 'hashtags': ['#tag1', '#tag2'], 'duration': 10},
    {'url': "url3", 'hashtags': ['#tag4', '#tag1', '#tag3', '#tag6'], 'duration': 10},
    {'url': "url4", 'hashtags': ['#tag4', '#tag1', '#tag3', '#tag6'], 'duration': 10},
]

memo = {}


# def calculate_score(video1, video2):
#     # get hashtags
#     hashtags1 = set(video1.get('hashtags', []))
#     hashtags2 = set(video2.get('hashtags', []))
#     intersection_score = len(hashtags1.intersection(hashtags2))
#     video1_score = len(hashtags1 - hashtags2)
#     video2_score = len(hashtags2 - hashtags1)
#     return min(intersection_score, video1_score, video2_score)


# def backtrack(video_list, temp_list, result, score):
#     if len(video_list) == len(temp_list):
#         result.append((temp_list[:], score))
#     # if len(temp_list) > len(video_list):
#     # return

#     for video in video_list:
#         temp_score = 0
#         if len(temp_list) == 0:
#             temp_score = 0
#         else:
#             # check if the engaing score is avaialble in the memo?
#             id1 = video.get('url')
#             id2 = temp_list[-1].get('url')
#             if f'{id1}{id2}' in memo:
#                 return memo[f'{id1}{id2}']
#             # evaluate score
#             temp_score = calculate_score(video, temp_list[-1])
#             # save the score in memo
#             memo[f'{id1}{id2}'] = temp_score
#             memo[f'{id2}{id1}'] = temp_score

#         temp_list.append(video)
#         backtrack(video_list, temp_list, result, score + temp_score)
#         temp_list.pop()


# def main(video_list):
#     result = []
#     backtrack(video_list, [], result, 0)
#     # result = sorted(result, key=lambda x: -x[1])[0]
#     print(result)
#     # return result


# res = main(v)
# print(res)


def calculate_score(video1, video2):
    # get hashtags
    hashtags1 = set(video1.get('hashtags', []))
    hashtags2 = set(video2.get('hashtags', []))
    intersection_score = len(hashtags1.intersection(hashtags2))
    video1_score = len(hashtags1 - hashtags2)
    video2_score = len(hashtags2 - hashtags1)
    return min(intersection_score, video1_score, video2_score)


def backtrack(result_list, temp_list, video_list, score):
    # Add condition here to validate the state before adding it to the result list
    if len(video_list) == 0:
        result_list.append((temp_list[:], score))

    for i in range(len(video_list)):
        temp_score = 0
        if len(temp_list[:]) > 0:
            # check if the engaing score is avaialble in the memo?
            id1 = video_list[i].get('url')
            id2 = temp_list[-1].get('url')

            if f'{id1}{id2}' in memo:
                temp_score = memo[f'{id1}{id2}']
            else:
                temp_score = calculate_score(video_list[i], temp_list[:][-1])
            # save the score in memo
            memo[f'{id1}{id2}'] = temp_score
            memo[f'{id2}{id1}'] = temp_score

        temp_list.append(video_list[i])
        backtrack(
            result_list,
            temp_list,
            video_list[:i] + video_list[i + 1 :],
            score + 0,
        )
        temp_list.pop()


def main_func(video_list):
    result_list = []
    backtrack(result_list, [], video_list, 0)
    return result_list


res = main_func(v)
print(res)
