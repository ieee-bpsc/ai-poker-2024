# Silicon Chip Smackdown

![Silicon Chip Smackdown Logo](logo.png)

This competition involves submitting a machine learning algorithm that can play a game of Texas hold'em poker against other agents. The performance of the models will also be tested against various given and hidden baseline models. The various conditions of the game will be provided to the participants.

## Submission Format

The first round of the event will be held **online**, and the code for your models have to submitted online. Your agent will have to extend a base agent class (BasePokerPlayer) and implement the methods of that class. The code for the base class is given below. For the specific details about the structure of the state and what return type is expected look at the section in the bottom of the document.

```python
#Look below for the strcuture of the various variables passed

class BasePokerPlayer:

    def declare_action(self, valid_actions, hole_card, round_state):
        call_action_info = valid_actions[1]
        action, amount = call_action_info["action"], call_action_info["amount"]
        return action, amount

    def receive_game_start_message(self, game_info):
        pass

    def receive_round_start_message(self, round_count, hole_card, seats):
        pass

    def receive_street_start_message(self, street, round_state):
        pass

    def receive_game_update_message(self, action, round_state):
        pass
        
    def receive_round_result_message(self, winners, hand_info, round_state):
        pass
```

## Setup

First, clone this repository. Then install the required packages in a new virtual environment by running the following lines -

```zsh
python -m venv env
source env/bin/activate
pip install -r requirements.txt
```

Make sure you are using **Python 3.12**. if you are using Windows, pywin32 might be an additional dependency as mentioned in the [requirements.txt](requirements.txt) file.

## Submission Conditions

**Submit a single python file** containing your model as a class called **CustomPokerPlayer** extending BasePokerPlayer. It must implement all the methods defined in BasePokerPlayer. If your model requires weights, they must be attached in a separate file and loaded into the model as part of receive_game_start_message.

- The models must be written in pytorch
- The models have to perform without being given user input
- The models will not have internet access
- Do not include any training or debug code, only the class definition as shown in the examples
- Your model must not have any dependencies outside of those specified in the requirements.txt file. If you wish to get a package added, please contact the organisers.

## Samples of callback arguments

#### `declare_action(self, valid_actions, hole_card, round_state)`

- valid_actions

```python
[

  {'action': 'fold', 'amount': 0},

  {'action': 'call', 'amount': 0},

  {'action': 'raise', 'amount': {'max': 95, 'min': 20}}

]

```

- hole_card

```python

['CA', 'DK']

```

- round_state

```python

{

  'round_count': 2,

  'dealer_btn': 1,

  'small_blind_pos': 2,

  'big_blind_pos': 0,

  'next_player': 0,

  'small_blind_amount': 10,

  'street': 'turn',

  'community_card': ['DJ', 'H6', 'S6', 'H5'],

  'seats': [

    {'stack': 95, 'state': 'participating', 'name': 'p1', 'uuid': 'ftwdqkystzsqwjrzvludgi'},

    {'stack': 20, 'state': 'participating', 'name': 'p2', 'uuid': 'bbiuvgalrglojvmgggydyt'},

    {'stack': 0, 'state': 'allin', 'name': 'p3', 'uuid': 'zkbpehnazembrxrihzxnmt'}

  ],

  'pot': {

    'main': {'amount': 165},

    'side': [{'amount': 20, 'eligibles': ['ftwdqkystzsqwjrzvludgi', 'bbiuvgalrglojvmgggydyt']}]

  }

  'action_histories': {

    'preflop': [

      {'action': 'ANTE', 'amount': 5, 'uuid': 'zkbpehnazembrxrihzxnmt'},

      {'action': 'ANTE', 'amount': 5, 'uuid': 'ftwdqkystzsqwjrzvludgi'},

      {'action': 'ANTE', 'amount': 5, 'uuid': 'bbiuvgalrglojvmgggydyt'},

      {'action': 'SMALLBLIND', 'amount': 10, 'add_amount': 10, 'uuid': 'zkbpehnazembrxrihzxnmt'},

      {'action': 'BIGBLIND', 'amount': 20, 'add_amount': 10, 'uuid': 'ftwdqkystzsqwjrzvludgi'},

      {'action': 'CALL', 'amount': 20, 'uuid': 'bbiuvgalrglojvmgggydyt', 'paid': 20},

      {'action': 'RAISE', 'amount': 30, 'add_amount': 10, 'paid': 20, 'uuid': 'zkbpehnazembrxrihzxnmt'},

      {'action': 'CALL', 'amount': 30, 'uuid': 'ftwdqkystzsqwjrzvludgi', 'paid': 10},

      {'action': 'CALL', 'amount': 30, 'uuid': 'bbiuvgalrglojvmgggydyt', 'paid': 10}

    ],

    'flop': [

      {'action': 'CALL', 'amount': 0, 'uuid': 'zkbpehnazembrxrihzxnmt', 'paid': 0},

      {'action': 'RAISE', 'amount': 30, 'add_amount': 30, 'paid': 30, 'uuid': 'ftwdqkystzsqwjrzvludgi'},

      {'action': 'CALL', 'amount': 30, 'uuid': 'bbiuvgalrglojvmgggydyt', 'paid': 30},

      {'action': 'CALL', 'amount': 20, 'uuid': 'zkbpehnazembrxrihzxnmt', 'paid': 20}

     ],

    'turn': [],

  }

}

```

#### `receive_game_start_message(self, game_info)`

- game_info

```python

{

  'player_num': 3,

  'rule': {

    'ante': 5,

    'blind_structure': {

      5 : { "ante": 10, "small_blind": 20 },

      7 : { "ante": 15, "small_blind": 30 }

    },

    'max_round': 10,

    'initial_stack': 100,

    'small_blind_amount': 10

  },

  'seats': [

    {'stack': 100, 'state': 'participating', 'name': 'p1', 'uuid': 'ftwdqkystzsqwjrzvludgi'},

    {'stack': 100, 'state': 'participating', 'name': 'p2', 'uuid': 'bbiuvgalrglojvmgggydyt'},

    {'stack': 100, 'state': 'participating', 'name': 'p3', 'uuid': 'zkbpehnazembrxrihzxnmt'}

  ]

}

```

#### `receive_round_start_message(self, round_count, hole_card, seats):`

- round_count

```python

2

```

- hole_card

```python

['C2', 'HQ']

```

- seats

```python

[

  {'stack': 135, 'state': 'participating', 'name': 'p1', 'uuid': 'ftwdqkystzsqwjrzvludgi'},

  {'stack': 80, 'state': 'participating', 'name': 'p2', 'uuid': 'bbiuvgalrglojvmgggydyt'},

  {'stack': 40, 'state': 'participating', 'name': 'p3', 'uuid': 'zkbpehnazembrxrihzxnmt'}

]

```

#### `receive_street_start_message(self, street, round_state)`

- street

```python

'preflop'

```

- round_state

```python

{

  'round_count': 1,

  'dealer_btn': 0,

  'small_blind_pos': 1,

  'big_blind_pos': 2,

  'next_player': 0,

  'small_blind_amount': 10,

  'street': 'preflop',

  'community_card': [],

  'seats': [

    {'stack': 95, 'state': 'participating', 'name': 'p1', 'uuid': 'ftwdqkystzsqwjrzvludgi'},

    {'stack': 85, 'state': 'participating', 'name': 'p2', 'uuid': 'bbiuvgalrglojvmgggydyt'},

    {'stack': 75, 'state': 'participating', 'name': 'p3', 'uuid': 'zkbpehnazembrxrihzxnmt'}

   ],

  'pot': {'main': {'amount': 45}, 'side': [] },

  'action_histories': {

    'preflop': [

      {'action': 'ANTE', 'amount': 5, 'uuid': 'bbiuvgalrglojvmgggydyt'},

      {'action': 'ANTE', 'amount': 5, 'uuid': 'zkbpehnazembrxrihzxnmt'},

      {'action': 'ANTE', 'amount': 5, 'uuid': 'ftwdqkystzsqwjrzvludgi'},

      {'action': 'SMALLBLIND', 'amount': 10, 'add_amount': 10, 'uuid': 'bbiuvgalrglojvmgggydyt'},

      {'action': 'BIGBLIND', 'amount': 20, 'add_amount': 10, 'uuid': 'zkbpehnazembrxrihzxnmt'}

    ]

  }

}

```

#### `receive_game_update_message(self, new_action, round_state)`

- new_action

```python

{

  'player_uuid': 'ftwdqkystzsqwjrzvludgi',

  'action': 'raise',

  'amount': 30

}

```

- round_state

```python

{

  'round_count': 2,

  'dealer_btn': 1,

  'small_blind_pos': 2,

  'big_blind_pos': 0,

  'next_player': 0,

  'small_blind_amount': 10,

  'street': 'flop',

  'community_card': ['DJ', 'H6', 'S6'],

  'seats': [

    {'stack': 95, 'state': 'participating', 'name': 'p1', 'uuid': 'ftwdqkystzsqwjrzvludgi'},

    {'stack': 50, 'state': 'participating', 'name': 'p2', 'uuid': 'bbiuvgalrglojvmgggydyt'},

    {'stack': 20, 'state': 'participating', 'name': 'p3', 'uuid': 'zkbpehnazembrxrihzxnmt'}

  ],

  'pot': {'main': {'amount': 135}, 'side': [] },

  'action_histories': {

    'preflop': [

      {'action': 'ANTE', 'amount': 5, 'uuid': 'zkbpehnazembrxrihzxnmt'},

      {'action': 'ANTE', 'amount': 5, 'uuid': 'ftwdqkystzsqwjrzvludgi'},

      {'action': 'ANTE', 'amount': 5, 'uuid': 'bbiuvgalrglojvmgggydyt'},

      {'action': 'SMALLBLIND', 'amount': 10, 'add_amount': 10, 'uuid': 'zkbpehnazembrxrihzxnmt'},

      {'action': 'BIGBLIND', 'amount': 20, 'add_amount': 10, 'uuid': 'ftwdqkystzsqwjrzvludgi'},

      {'action': 'CALL', 'amount': 20, 'uuid': 'bbiuvgalrglojvmgggydyt', 'paid': 20},

      {'action': 'RAISE', 'amount': 30, 'add_amount': 10, 'paid': 20, 'uuid': 'zkbpehnazembrxrihzxnmt'},

      {'action': 'CALL', 'amount': 30, 'uuid': 'ftwdqkystzsqwjrzvludgi', 'paid': 10},

      {'action': 'CALL', 'amount': 30, 'uuid': 'bbiuvgalrglojvmgggydyt', 'paid': 10}

    ],

    'flop': [

      {'action': 'CALL', 'amount': 0, 'uuid': 'zkbpehnazembrxrihzxnmt', 'paid': 0},

      {'action': 'RAISE', 'amount': 30, 'add_amount': 30, 'paid': 30, 'uuid': 'ftwdqkystzsqwjrzvludgi'}

    ]

  }

}

```

#### `receive_round_result_message(self, winners, hand_info, round_state)`

- winners

```python

[

  {'stack': 300, 'state': 'participating', 'name': 'p1', 'uuid': 'ftwdqkystzsqwjrzvludgi'}

]

```

- hand_info

```python

[

  {

    'uuid': 'ftwdqkystzsqwjrzvludgi',

    'hand': {

      'hole': {'high': 14, 'low': 13},

      'hand': {'high': 6, 'strength': 'ONEPAIR', 'low': 0}

    }

  },

  {

    'uuid': 'bbiuvgalrglojvmgggydyt',

    'hand': {

      'hole': {'high': 12, 'low': 2},

      'hand': {'high': 6, 'strength': 'ONEPAIR', 'low': 0}

    }

  },

  {

    'uuid': 'zkbpehnazembrxrihzxnmt',

    'hand': {

      'hole': {'high': 10, 'low': 3},

      'hand': {'high': 6, 'strength': 'ONEPAIR', 'low': 0}

    }

  }

]

```

- round_state

```python

{

  'dealer_btn': 1,

  'big_blind_pos': 0,

  'round_count': 2,

  'small_blind_pos': 2,

  'next_player': 0,

  'small_blind_amount': 10,

  'action_histories': {

    'turn': [

      {'action': 'CALL', 'amount': 0, 'uuid': 'ftwdqkystzsqwjrzvludgi', 'paid': 0},

      {'action': 'RAISE', 'amount': 20, 'add_amount': 20, 'paid': 20, 'uuid': 'bbiuvgalrglojvmgggydyt'},

      {'action': 'CALL', 'amount': 20, 'uuid': 'ftwdqkystzsqwjrzvludgi', 'paid': 20}

    ],

    'preflop': [

      {'action': 'ANTE', 'amount': 5, 'uuid': 'zkbpehnazembrxrihzxnmt'},

      {'action': 'ANTE', 'amount': 5, 'uuid': 'ftwdqkystzsqwjrzvludgi'},

      {'action': 'ANTE', 'amount': 5, 'uuid': 'bbiuvgalrglojvmgggydyt'},

      {'action': 'SMALLBLIND', 'amount': 10, 'add_amount': 10, 'uuid': 'zkbpehnazembrxrihzxnmt'},

      {'action': 'BIGBLIND', 'amount': 20, 'add_amount': 10, 'uuid': 'ftwdqkystzsqwjrzvludgi'},

      {'action': 'CALL', 'amount': 20, 'uuid': 'bbiuvgalrglojvmgggydyt', 'paid': 20},

      {'action': 'RAISE', 'amount': 30, 'add_amount': 10, 'paid': 20, 'uuid': 'zkbpehnazembrxrihzxnmt'},

      {'action': 'CALL', 'amount': 30, 'uuid': 'ftwdqkystzsqwjrzvludgi', 'paid': 10},

      {'action': 'CALL', 'amount': 30, 'uuid': 'bbiuvgalrglojvmgggydyt', 'paid': 10}

    ],

    'river': [],

    'flop': [

      {'action': 'CALL', 'amount': 0, 'uuid': 'zkbpehnazembrxrihzxnmt', 'paid': 0},

      {'action': 'RAISE', 'amount': 30, 'add_amount': 30, 'paid': 30, 'uuid': 'ftwdqkystzsqwjrzvludgi'},

      {'action': 'CALL', 'amount': 30, 'uuid': 'bbiuvgalrglojvmgggydyt', 'paid': 30},

      {'action': 'CALL', 'amount': 20, 'uuid': 'zkbpehnazembrxrihzxnmt', 'paid': 20}

    ]

  },

  'street': 'showdown',

  'seats': [

    {'stack': 300, 'state': 'participating', 'name': 'p1', 'uuid': 'ftwdqkystzsqwjrzvludgi'},

    {'stack': 0, 'state': 'allin', 'name': 'p2', 'uuid': 'bbiuvgalrglojvmgggydyt'},

    {'stack': 0, 'state': 'allin', 'name': 'p3', 'uuid': 'zkbpehnazembrxrihzxnmt'}

  ],

  'community_card': ['DJ', 'H6', 'S6', 'H5', 'C4'],

  'pot': {

    'main': {'amount': 165},

    'side': [

      {'amount': 60, 'eligibles': ['ftwdqkystzsqwjrzvludgi', 'bbiuvgalrglojvmgggydyt'] },

      {'amount': 0, 'eligibles': ['ftwdqkystzsqwjrzvludgi', 'bbiuvgalrglojvmgggydyt'] }

    ]

  }

}

```
