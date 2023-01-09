def remove_url_anchor(url):
    sep = '#'
    return url.split(sep, 1)[0]