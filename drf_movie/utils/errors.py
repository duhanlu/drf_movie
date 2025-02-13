
def response_data(status_code=0, message=None, data={}, **kwargs):
    return dict({
        'status_code': status_code,
        'message': message,
        'data': data,
    }, **kwargs)
class MovieError():
    MovieNotFound = (10001, 'Movie is not found')
    MovieCollectFail = (10002, 'Moive collection failure')
    

class UserError():
    UserNotFound = (20001, 'User not exist')
    CancelMovieFailed = (10003, 'Cannot Cancel Movie')
    NotCollectedMovie = (10004, 'Did not collect the movie')
    
class TradeError():
    CardParamsError = (30001, 'membership parameters error')
    OrderCreateError = (30002, 'order create error')
    PayRequestError = (30003, 'payment request error')
    ProfileNotFoundError = (30004, 'profile is not found')