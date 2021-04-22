from cleaner import clean
import champion_filter as filter
from win_rate import calculate_winrate as win_rate

# config
config = {
    'clean': {
        "enabled": True,
        "original": '../data/pre-cleaning-dataset.csv',
        "cleaned": '../data/post-cleaning-dataset.csv'
    },
    'filter_champions': {
        "enabled": True,
        'champion_dictionary': "../data/champions-cleaned.json",
        'output': "../data/filtered-dataset.csv",
        'output-no-header': "../data/filtered-dataset-no-header.csv",
        'desired_columns': [
            'teams.0.win',
            'participants.0.championId',
            'participants.1.championId',
            'participants.2.championId',
            'participants.3.championId',
            'participants.4.championId',
            'participants.5.championId',
            'participants.6.championId',
            'participants.7.championId',
            'participants.8.championId',
            'participants.9.championId', ],
    },
    'win_rate': {
        'enabled': True,
        'output': '../data/win_rate.txt'
    }
}


def main():
    if config['clean']["enabled"]:
        print('Cleaning the dataset...')
        clean(config['clean']['original'], config['clean']['cleaned'])
    if config['filter_champions']["enabled"]:
        print('Filtering champion data from the dataset...')
        filter.filter(config['clean']["cleaned"], config['filter_champions']["output"],
                      config['filter_champions']["desired_columns"], config['filter_champions']["champion_dictionary"], True)
        print('Filtering champion data from the dataset...')
        filter.filter(config['clean']["cleaned"], config['filter_champions']["output-no-header"],
                                config['filter_champions']["desired_columns"],
                                config['filter_champions']["champion_dictionary"], False)
    if config['win_rate']['enabled']:
        print('Computing the winrate...')
        win_rate(config['filter_champions']['output'], config['win_rate']['output'])


if __name__ == '__main__':
    main()
