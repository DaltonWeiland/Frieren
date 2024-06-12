def ShowRecommendations(shownum):
    if shownum % 10 == 0:
        return "Show 1"
    
    if shownum % 10 == 1:
        return "Show2"
    else:
        return "Show UNDEF"