def search_images(search_term, page, folder, max_results=250, group_size=50, total=0):
    ''' Search Bing API for images.
    max_n: is the number of images to download,
    count: number of queries per page,
    search_term: query to search for in Bing Images
    page: start page,
    folder: path to repo
    total: total number downloaded
    '''

    import requests
    import matplotlib.pyplot as plt
    from PIL import Image
    from io import BytesIO
    from requests import exceptions
    from time import sleep
    import os


    subscription_key = open('/Users/angela/Documents/Resources/azure.txt', 'r').read().strip()
    search_url = 'https://api.cognitive.microsoft.com/bing/v7.0/images/search'

    exceptions = set([IOError, FileNotFoundError,
                      exceptions.RequestException, exceptions.HTTPError,
                      exceptions.ConnectionError, exceptions.Timeout])

    headers = {"Ocp-Apim-Subscription-Key" : subscription_key}

    params = {'q': search_term, 'offset': page, 'count': group_size, 'imageType': 'photo'}

    for offset in range(page, max_results, group_size):
        print(f'Making request for group {offset}-{offset + group_size} of {max_results}...')
        params['offset'] = offset
        res = requests.get(search_url, headers=headers, params=params)
        res.raise_for_status()
        search_results = res.json()
        print(f'Saving images for group {offset}-{offset + group_size} of {max_results}...')

        # loop over the results
        for v in search_results['value']:
            try:
                # make a request to download the image
                print('Downloading: {}'.format(v['contentUrl']))
                r = requests.get(v['contentUrl'], timeout=30)

                # build the path to the output image
                ext = v['contentUrl'][v["contentUrl"].rfind('.'):]
                p = os.path.sep.join([folder, f'{str(total).zfill(8)}{ext}'])

                # write the image to disk
                f = open(p, "wb")
                f.write(r.content)
                f.close()

            # catch any errors that would not unable us to download the image
            except Exception as e:
                if type(e) in exceptions:
                    print('Skipping: {}'.format(v['contentUrl']))
                    continue

            total += 1
            sleep(3)
    print(f'Total images downloaded: {total}')