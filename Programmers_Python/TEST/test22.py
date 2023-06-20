import requests


def multiply(a, b, bound):
    # write your code here

    return 0


# def topArticles(limit):
#     response = requests.get('https://jsonmock.hackerrank.com/api/articles?page=' + str(limit))
#     print(response)
#     print(response.json())
#
#     return


import requests as rq


def topArticles(limit):
    # Write your code here
    page = 0
    articles = []
    while True:
        page += 1
        path = f"https://jsonmock.hackerrank.com/api/articles?page={page}"
        r = rq.get(path)
        res = r.json()['data']
        if not res:
            break
        for atc in res:
            atc_info = dict()
            if atc['title'] is None and atc['story_title'] is None:
                continue
            elif atc['title'] is None:
                atc_info['title'] = atc['story_title']
            else:
                atc_info['title'] = atc['title']
            if atc['num_comments'] is None:
                atc_info['num_comments'] = 0
            else:
                atc_info['num_comments'] = atc['num_comments']

            articles.append(atc_info)
    # print('articles:', articles)
    answer = sorted(articles, key=lambda x: (-x['num_comments'], x['title']))[:limit]

    return [x['title'] for x in answer]


def max_Sum_arr_len_k(arr, length, k):
    win_sum = 0
    ans = 0
    for index in range(0, length):
        win_sum = win_sum + arr[index]
        if index >= k:
            win_sum = win_sum - arr[index - k]
        if index >= k - 1:
            ans = max(ans, win_sum)
    return ans


def getMaxProfit(pnl, k):
    length = len(pnl)
    ans = 0
    for index in range(1, k + 1):
        current_max_sum = max_Sum_arr_len_k(pnl, length, index)
        ans = max(ans, current_max_sum)
    return ans


def multiply(a, b, bound):
    # write your code here
    res = a * b
    if res > bound:
        raise ValueError('multiplication of %s and %s with bound %s not possible' % (a, b, bound))
    else:
        return res


if __name__ == '__main__':
    print(topArticles(2))
