'''Players Classes to define individual players.
Two parent classes - OPlayer and DPlayer

'''


class OPlayer:
    '''Dosctring TODO
    THIS IS NOT A VERY GENERALIZABLE MODEL IF YOU KNOW THINGS ABOUT FOOTBALL
    and that's okay
    '''
    def __init__(self, name=None, yards=120, touchdowns=5, catches=4):
        self.name = name
        self.stats = {'td': touchdowns,
                      'yards': yards,
                      'catches': catches}

    def get_points(self):
        '''Gets points scored by the player from stats
        '''
        td_points = 6 * self.stats['td']
        yards_points = self.stats['yards']
        catch_points = 2 * self.stats['catches']
        total_points = td_points + yards_points + catch_points
        return total_points


class Quarterback(OPlayer):
    '''Override certain parameters of the default OPlayer class and add some
    functionality unique to quarterbacks
    '''
    def __init__(self, name=None, yards=130, touchdowns=5, completed_passes=20,
                 interceptions=2, sacks=1):
        super().__init__(name=name, yards=yards, touchdowns=touchdowns)
        self.completed_passes = completed_passes
        self.interceptions = interceptions
        self.sacks = sacks

    def passing_score(self):
        '''This is a random formula... FYI
        '''
        pass_score = self.completed_passes - (2 * (
                                            self.interceptions + self.sacks))
        score = pass_score + OPlayer.get_points(self)
        return score


class Kicker(OPlayer):
    ''' Override some default parameters and add specific stats for kickers
    (yards refers to total made fg yards)
    '''
    def __init__(self, name=None, yards=60, field_goals=2, missed_fg=1,
                 touchdowns=0):
        super().__init__(name=name, yards=yards, touchdowns=touchdowns)
        self.field_goals = field_goals
        self.missed_fg = missed_fg

    def kicking_score(self):
        kick_score = self.field_goals - self.missed_fg
        score = kick_score + OPlayer.get_points(self)
        return score


class DPlayer:
    '''
    Class for individual defensive players
    '''
    def __init__(self, tackles=5, sacks=0.5, interceptions=0, fumble=0,
                 safety=0):
        self.tackles = tackles
        self.sacks = sacks
        self.interceptions = interceptions
        self.fumbles = fumbles

    def get_points(self):
        '''
        get points scored by defensive player
        '''
        tackle_points = self.tackles
        sack_points = 3 * self.sacks
        turnover_points = (5 * self.interceptions) + (5 * self.fumbles)
