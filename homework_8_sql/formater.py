def tracks_length_to_html(lst):

    from datetime import timedelta
    result = '<h2>Total tracks length by genres:</h2>'
    for genre, mls in lst:
        result += f'<b>{genre}</b>: {timedelta(milliseconds=mls)}'
        result = result.replace(result[result.find('.'):], '<br>')
    return result


def top_sale_tracks_to_html(lst):

    result = f'<h2>Top sale tracks with sum:</h2>'
    for track_name, sum in lst:
        result += f'<br>{track_name}: <b>{sum}</b>'
    return result