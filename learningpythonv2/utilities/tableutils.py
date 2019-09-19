from prettytable import PrettyTable


class PrettyTableGenerator:
    def getTable(businessProfiles):
        if businessProfiles is None:
            raise Exception('Invalid Business Profiles Collection Specified!')

        table = PrettyTable(['Id', 'Name', 'City', 'Email', 'Phone'])

        for businessProfile in businessProfiles:
            table.add_row([
                businessProfile.id, businessProfile.fullName,
                businessProfile.city, businessProfile.email, businessProfile.phone])

        return table
