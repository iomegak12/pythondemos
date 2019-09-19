import models


class BusinessProfileEncoder:
    def transform(dict):
        if(dict is None):
            raise Exception('Invalid Argument Specified!')

        businessProfile = models.BusinessProfile(
            dict['id'], dict['fullName'], dict['avatar'],
            dict['city'], dict['email'], dict['phone'])

        return businessProfile
