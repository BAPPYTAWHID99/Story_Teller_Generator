GENRE_CHOICES = [
    ('Fantasy', 'Fantasy'),
    ('Adventure', 'Adventure'),
    ('Mystery', 'Mystery'),
    ('Horror', 'Horror'),
    ('Science Fiction', 'Science Fiction'),
    ('Romance', 'Romance'),
    ('Comedy', 'Comedy'),
    ('Drama', 'Drama'),
    ('Historical', 'Historical'),
    ('Thriller', 'Thriller'),
]

MOOD_CHOICES = [
    ('Adventure', 'Adventure'),
    ('Funny', 'Funny'),
    ('Dark', 'Dark'),
    ('Emotional', 'Emotional'),
    ('Inspirational', 'Inspirational'),
    ('Mysterious', 'Mysterious'),
    ('Romantic', 'Romantic'),
    ('Suspenseful', 'Suspenseful'),
    ('Hopeful', 'Hopeful'),
]

STORY_LENGTH_CHOICES = [
    ('Short', 'Short'),
    ('Medium', 'Medium'),
    ('Long', 'Long'),
]

LENGTH_CONFIG = {
    'Short': {'min_words': 250, 'max_words': 400},
    'Medium': {'min_words': 500, 'max_words': 700},
    'Long': {'min_words': 900, 'max_words': 1200},
}

GENRE_DATA = {
    'Fantasy': {
        'settings': [
            'an ancient citadel hidden beneath moonlit cliffs',
            'a floating market suspended over an enchanted river',
            'a city where towers glow with living crystal',
            'a hidden valley guarded by old spellbound gates',
        ],
        'conflicts': [
            'a forgotten prophecy awakening beneath the streets',
            'an ancient machine stirring with forbidden magic',
            'a tyrant seeking the power buried in the city walls',
            'a curse that began when the stars were misaligned',
        ],
        'events': [
            'the protagonist discovered a sealed chamber full of stories',
            'an old mentor revealed a map hidden in a clocktower',
            'rival guilds chased the team through illuminated alleys',
            'the city itself answered the call with moving bridges',
        ],
        'endings': [
            'the city was restored to peace beneath a dawn of silver fire',
            'the hidden prophecy was fulfilled without sacrificing the living',
            'the people formed a new alliance to protect the realm',
            'the ancient magic chose a kinder future for all',
        ],
    },
    'Adventure': {
        'settings': [
            'a canyon carved by thunder and time',
            'a coastal port crowded with traders and legends',
            'a jungle valley alive with hidden ruins',
            'a mountain road leading to a forgotten outpost',
        ],
        'conflicts': [
            'a stolen relic that could change the region forever',
            'a treacherous route blocked by storms and rivals',
            'a dangerous expedition into uncharted wilderness',
            'an impossible race against a collapsing bridge',
        ],
        'events': [
            'a scouting party uncovered a route through the cliffs',
            'the team crossed a ravine using ropes and teamwork',
            'a storm forced them to shelter in an abandoned watchtower',
            'the protagonist solved a puzzle left by an old explorer',
        ],
        'endings': [
            'the expedition returned with a glowing map and renewed courage',
            'the lost route became a safer trail for future travelers',
            'the adventure ended with a shared celebration by the fire',
            'the treasure proved to be knowledge rather than gold',
        ],
    },
    'Mystery': {
        'settings': [
            'a rain-soaked district of locked doors and whispered rumors',
            'an abandoned train station with a single clock still running',
            'a lighthouse overlooking a fog-filled bay',
            'a mansion with rooms that never appeared on the same floor twice',
        ],
        'conflicts': [
            'a missing heirloom tied to an old disappearance',
            'a pattern of clues that seemed written by someone long dead',
            'an impossible theft committed with no visible entrance',
            'a city-wide rumor that pointed to a single hidden witness',
        ],
        'events': [
            'the protagonist found an unusual cipher in a pocket watch',
            'a hidden ledger revealed a pattern in the town records',
            'the investigation narrowed to one night of storms and silence',
            'old friends became suspects before the truth emerged',
        ],
        'endings': [
            'the mystery was solved with a final confession in the lantern room',
            'the missing truth returned the family name to honor',
            'the city finally learned the real story behind its oldest rumor',
            'the hidden culprit was exposed by mercy and evidence alike',
        ],
    },
    'Horror': {
        'settings': [
            'a dilapidated asylum beneath a frozen hill',
            'a church with a bell that rings without a rope',
            'a narrow tunnel beneath a drowned neighborhood',
            'a mansion whose windows reflect a different century',
        ],
        'conflicts': [
            'an evil memory returning through the walls',
            'a creature that only appears when the lights fail',
            'a family curse tied to a single child and a hidden room',
            'the sound of footsteps following every person home',
        ],
        'events': [
            'the protagonist followed a smell of roses into a sealed cellar',
            'a ritual was interrupted by a whisper from the floorboards',
            'the group discovered old photographs showing faces erased by time',
            'a frightened witness exposed the real source of the terror',
        ],
        'endings': [
            'the house finally went silent when the truth was spoken aloud',
            'the curse ended only when the last hidden secret was revealed',
            'the survivors left with a warning never to return after sunset',
            'the darkness retreated, but the memory remained',
        ],
    },
    'Science Fiction': {
        'settings': [
            'an orbital garden hanging above a dying moon',
            'a submerged city powered by the tide and old reactors',
            'a research arcology built beneath a frozen desert',
            'a colony world where the sky glows with artificial dawn',
        ],
        'conflicts': [
            'an AI discovering a hidden archive of human history',
            'a core reactor cracking under a strain no one expected',
            'a transmission from deep space revealing a forgotten stasis ship',
            'a political rift splitting the colony over a new energy source',
        ],
        'events': [
            'the protagonist calibrated an abandoned drone system to map the undercity',
            'a signal from an unknown star led the crew to a buried archive',
            'the colony discovered that its weather engines were still alive',
            'an emergency launch revealed the true origin of the city',
        ],
        'endings': [
            'the city survived by choosing cooperation over control',
            'the colony learned to share power instead of hoard it',
            'the hidden archive became a guide for a better future',
            'the first signal became the beginning of a new era',
        ],
    },
    'Romance': {
        'settings': [
            'a seaside town where every street lights up at dusk',
            'a cramped bookstore above a blooming square',
            'a countryside inn built beside a river of wild orchids',
            'a grand old theatre where the curtains always whisper',
        ],
        'conflicts': [
            'two people separated by duty, timing, and fear',
            'a secret letter arriving too late to explain the past',
            'family expectations pressing on a relationship',
            'a sudden departure that tests whether love can survive distance',
        ],
        'events': [
            'the main characters met through a shared misunderstanding and laughter',
            'a handwritten note revealed feelings that had been hidden for years',
            'a festival night forced them to choose honesty over comfort',
            'old wounds were mended beneath lantern light and music',
        ],
        'endings': [
            'their love became a steady promise rather than a brief spark',
            'the town witnessed a wedding beneath the first warm rain of spring',
            'they chose a future built on understanding and patience',
            'the final chapter promised a new beginning with open hearts',
        ],
    },
    'Comedy': {
        'settings': [
            'a small town where every festival becomes a competition',
            'a bakery famous for impossible pastries and louder gossip',
            'a struggling theatre filled with mismatched performers',
            'a local market where no bargain is ever straightforward',
        ],
        'conflicts': [
            'a perfect plan ruined by a chain of accidental mishaps',
            'a misunderstanding escalating into a town-wide confusion',
            'a last-minute contest that no one can afford to lose',
            'a secret identity revealed at the worst possible moment',
        ],
        'events': [
            'the protagonist attempted a clever scheme and somehow made it worse',
            'a costume mix-up caused a comic misunderstanding across the town',
            'everyone chased the same rumor until the rumor chased them back',
            'an accident turned into the best idea anyone had ever heard',
        ],
        'endings': [
            'the town laughed so hard it became a better place',
            'the chaos was transformed into a story everyone retold',
            'everyone accepted the mistake and left grinning',
            'the entire plan succeeded because it was ridiculous enough to work',
        ],
    },
    'Drama': {
        'settings': [
            'a valley torn between memories and economic ruin',
            'a neighborhood holding onto tradition while the world changes',
            'a hospital ward where every patient tells a different version of hope',
            'a family estate crowded with silences and old loans',
        ],
        'conflicts': [
            'a decision that would change a family forever',
            'a buried truth threatening to break a long-held peace',
            'a dream for change colliding with the cost of survival',
            'a community split between loyalty and justice',
        ],
        'events': [
            'a final conversation revealed the depth of old betrayals',
            'the protagonist returned home only to discover what was missing',
            'a quiet act of bravery changed the path of everyone nearby',
            'a vulnerable choice opened the possibility of forgiveness',
        ],
        'endings': [
            'the family rebuilt something honest from sorrow',
            'a hard truth became the start of healing rather than damage',
            'the town remembered its humanity in the middle of crisis',
            'the final scene held both grief and grace in balance',
        ],
    },
    'Historical': {
        'settings': [
            'a frontier town under the shadow of an empire',
            'a cathedral city recovering from a bitter siege',
            'a caravan route connecting kingdoms through desert heat',
            'a harbor where ships carry both news and rebels',
        ],
        'conflicts': [
            'a kingdom teetering on the edge of civil unrest',
            'a forbidden map that could shift the balance of power',
            'a siege that ended any illusion of safety',
            'a family name caught between loyalty and rebellion',
        ],
        'events': [
            'the protagonist found evidence in an archive left behind by war',
            'a hidden courtship crossed social boundaries and danger',
            'the city faced a difficult winter and an even greater choice',
            'an old oath drove the characters toward a decision of honor',
        ],
        'endings': [
            'the region emerged wiser after the conflict',
            'the people chose justice over fear at last',
            'a difficult peace was crafted from sacrifice',
            'history was rewritten by the courage of a single act',
        ],
    },
    'Thriller': {
        'settings': [
            'a transit hub where every departure smells of danger',
            'a private tower above a city that never sleeps',
            'a storm-damaged hospital with locked wards and burned files',
            'a research campus where hidden data never stays hidden',
        ],
        'conflicts': [
            'a conspiracy tightening around a single witness',
            'a countdown to an impossible breach no one can stop',
            'an anonymous voice leading the heroes toward a trap',
            'a secret network operating inside the city itself',
        ],
        'events': [
            'the protagonist followed a trail of stolen records to a hidden office',
            'a midnight escape turned into a chase through reflecting corridors',
            'a trusted ally revealed a startling conflict of interest',
            'the final clue surfaced only after the power grid failed',
        ],
        'endings': [
            'the truth surfaced just before the city was lost to fear',
            'the conspiracy was dismantled in a single decisive night',
            'the witness survived long enough to expose the real enemy',
            'the silence after the storm was the sound of a city waking up',
        ],
    },
}
