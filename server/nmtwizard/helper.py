import random
import json
import uuid

adjectives = [
    "Able", "Acceptable", "Accurate", "Acidic", "Active", "Actual", "Additional",
    "Administrative", "Agreeable", "Alive", "Alternative",
    "Amazing", "Ambitious", "Ancient", "Angry", "Annual", "Another", "Appropriate",
    "Asleep", "Attractive", "Automatic", "Available", "Aware", "Basic", "Beautiful", "Best",
    "Bewildered", "Big", "Bitter", "Black", "Blue", "Born", "Brave", "Breezy", "Brief",
    "Bright", "Brilliant", "Broad", "Brown", "Bumpy", "Busy", "Calm", "Capable", "Capital",
    "Careful",
    "Cheap", "Chemical", "Chilly", "Chubby", "Civil", "Classic", "Clean", "Clear",
    "Clever", "Clumsy", "Cold", "Colossal", "Comfortable", "Commercial", "Common", "Competitive",
    "Complete", "Complex", "Comprehensive", "Confident", "Conscious", "Consistent", "Constant",
    "Content", "Cool", "Correct", "Crazy", "Creamy", "Creative", "Critical", "Cuddly", "Cultural",
    "Curious", "Current", "Curved", "Cute", "Dangerous",
    "Dazzling", "Deafening", "Dear", "Decent", "Defeated", "Delicious", "Delightful",
    "Different", "Direct", "Distinct", "Double", "Dramatic", "Dry",
    "Eager", "Early", "East", "Eastern", "Educational", "Effective", "Efficient",
    "Electrical", "Electronic", "Elegant", "Embarrassed", "Emotional", "Empty", "Entire",
    "Environmental", "Equal", "Equivalent", "Even", "Exact", "Excellent", "Exciting",
    "Existing", "Expensive", "Expert", "Express", "Extension", "External", "Extra", "Extreme",
    "Faint",
    "Fair", "Faithful", "False", "Familiar", "Famous", "Fancy", "Fast", "Federal", "Fierce",
    "Final", "Financial", "Fine", "Firm", "First", "Fit", "Flaky", "Flat", "Fluffy",
    "Foreign", "Formal", "Former", "Free", "Freezing", "Frequent", "Fresh", "Friendly", "Full",
    "Fun",
    "Funny", "Future", "General", "Gentle", "Gifted", "Gigantic", "Glad", "Glamorous",
    "Global", "Gold", "Golden", "Good", "Gorgeous", "Grand", "Gray", "Great", "Green",
    "Grumpy", "Guilty", "Hallowed", "Handsome", "Happy", "Healthy", "Heavy",
    "Helpful", "Helpless", "High", "Hissing", "Historical", "Hollow", "Honest",
    "Howling", "Huge", "Hungry", "Icy", "Ideal", "Immediate", "Immense", "Important",
    "Impossible", "Impressive", "Independent", "Individual", "Inevitable", "Informal",
    "Initial", "Inner", "Inside", "Intelligent", "Interesting", "Internal", "International",
    "Jolly", "Juicy", "Junior", "Kind", "Known", "Large",
    "Last", "Late", "Leading", "Least", "Left", "Legal", "Level",
    "Little", "Live", "Lively", "Living", "Local", "Logical", "Long", "Lost",
    "Loud", "Low", "Lower", "Lucky", "Mad", "Magnificent", "Main", "Major", "Massive", "Master",
    "Maximum", "Mealy", "Medium", "Melodic", "Melted", "Microscopic",
    "Middle", "Miniature", "Minimum", "Minor", "Modern",
    "More", "Muscular", "Mushy", "Mysterious", "Narrow", "National", "Native",
    "Natural", "Neat", "Necessary", "Nervous", "New", "Nice", "Noisy",
    "Normal", "North", "Novel", "Numerous", "Nutritious", "Nutty", "Obedient", "Objective",
    "Obnoxious",
    "Obvious", "Odd", "Official", "Old", "Open", "Opposite", "Orange", "Ordinary", "Original",
    "Particular", "Past", "Patient", "Perfect", "Personal", "Petite",
    "Physical", "Plain", "Pleasant", "Plenty", "Polite", "Political",
    "Popular", "Positive", "Possible", "Potential", "Powerful", "Practical", "Prehistoric",
    "Pretty",
    "Previous", "Prickly", "Primary", "Prior", "Private", "Prize", "Professional", "Proper",
    "Proud",
    "Psychological", "Public", "Puny", "Pure", "Purple", "Purring", "Putrid", "Quaint", "Quick",
    "Quiet",
    "Rancid", "Rapid", "Rare", "Raspy", "Real", "Realistic", "Reasonable", "Red", "Refined",
    "Regular",
    "Relative", "Relevant", "Remarkable", "Remote", "Responsible", "Rhythmic", "Rich", "Right",
    "Ripe",
    "Rough", "Round", "Royal", "Sad", "Safe", "Salty", "Scared", "Scary",
    "Screeching", "Scruffy", "Secret", "Secure", "Select", "Senior", "Sensitive", "Separate",
    "Serious",
    "Severe", "Shallow", "Shapely", "Sharp", "Short", "Shrilling", "Shy", "Signal",
    "Significant", "Silly", "Silver", "Similar", "Simple", "Single", "Slight", "Slow", "Small",
    "Smart", "Smooth", "Soft", "Solid", "Sour", "South", "Southern", "Spare", "Special",
    "Specialist", "Specific", "Spicy", "Spiritual", "Square", "Squeaking", "Stale", "Standard",
    "Steep",
    "Sticky", "Still", "Stock", "Stocky", "Straight", "Strange", "Street", "Strict", "Strong",
    "Substantial",
    "Successful", "Sudden", "Sufficient", "Suitable", "Super", "Sure", "Suspicious", "Sweet",
    "Swift", "Swimming",
    "Tall", "Tasteless", "Technical", "Teeny", "Temporary", "Tender", "Terrible",
    "Thankful", "Thick", "Thin", "Thoughtless", "Thundering", "Tinkling", "Tiny", "Top",
    "Tough", "Traditional", "Training", "Tricky", "True", "Typical", "Unique", "United", "Unkempt",
    "Unusual",
    "Upper", "Useful", "Usual", "Valuable", "Various", "Vast", "Victorious", "Visible", "Visual",
    "Wailing",
    "Warm", "Waste", "Weak", "Weekly", "Weird", "West", "Western", "Whispering", "White", "Wide",
    "Wild", "Willing", "Winter", "Wise", "Witty", "Wonderful", "Worried", "Worth",
    "Yellow", "Young", "Zealous"]

nouns = [
    "Aardvark", "Aardwolf", "Albatross", "Alligator", "Alpaca", "Anaconda", "Anglerfish", "Ant",
    "Anteater",
    "Antelope", "Antlion", "Ape", "Aphid", "Armadillo", "Asp", "Axolotl", "Baboon", "Badger",
    "Bandicoot", "Barnacle",
    "Barracuda", "Basilisk", "Bass", "Bat", "Beaver", "Bedbug", "Bee", "Beetle", "Bison",
    "Blackbird", "Boa", "Bobcat",
    "Bobolink", "Bonobo", "Bovid", "Buffalo", "Bug", "Bull", "Butterfly", "Buzzard", "Camel",
    "Canid",
    "Capybara", "Cardinal", "Caribou", "Carp", "Caterpillar", "Catfish", "Catshark", "Centipede",
    "Cephalopod",
    "Chameleon", "Cheetah", "Chickadee", "Chimpanzee", "Chinchilla", "Chipmunk", "Cicada", "Clam",
    "Clownfish",
    "Coati", "Cobra", "Cockroach", "Cod", "Condor", "Constrictor", "Coral", "Cougar", "Cow",
    "Coyote", "Coypu",
    "Crab", "Crane", "Crawdad", "Crayfish", "Cricket", "Crocodile", "Crow", "Cuckoo", "Damselfly",
    "Deer", "Dhole",
    "Dingo", "Dodo", "Dolphin", "Dormouse", "Dove", "Dragon", "Dragonfly", "Eagle", "Earthworm",
    "Earwig", "Echidna",
    "Eel", "Egret", "Elephant", "Elk", "Emu", "Ermine", "Falcon", "Fennec", "Ferret", "Finch",
    "Firefly", "Fish",
    "Flamingo", "Flea", "Fly", "Flyingfish", "Fowl", "Fox", "Frog", "Gazelle", "Gecko", "Gerbil",
    "Gibbon", "Giraffe",
    "Goldfish", "Gopher", "Gorilla", "Grasshopper", "Grebe", "Grouse", "Guanaco", "Gull", "Guppy",
    "Haddock", "Halibut",
    "Hamster", "Hare", "Harrier", "Hawk", "Hedgehog", "Heron", "Herring", "Hippopotamus",
    "Hookworm", "Hornet", "Hoverfly",
    "Human", "Hummingbird", "Hyena", "Hyrax", "Ibis", "Iguana", "Jacana", "Jackal", "Jaguar", "Jay",
    "Joey", "Jellyfish", "Kangaroo",
    "Kingfisher", "Kite", "Kiwi", "Koala", "Koi", "Krill", "Ladybug", "Lamprey", "Landfowl",
    "Lapwing", "Lark", "Leech",
    "Lemming", "Lemur", "Leopard", "Leopon", "Limpet", "Lion", "Lionfish", "Lizard", "Llama",
    "Lobster", "Locust", "Loon",
    "Loris", "Louse", "Lungfish", "Lynx", "Macaw", "Mackerel", "Magpie", "Mallard", "Manatee",
    "Mandrill", "Marlin",
    "Marmoset", "Marmot", "Marsupial", "Marten", "Mastodon", "Maya", "Meadowlark", "Meerkat",
    "MiMi", "Mink", "Minnow", "Mite",
    "Mockingbird", "Mollusk", "Mongoose", "Monkey", "Moose", "Mosquito", "Moth", "Mouse", "Mule",
    "Muskox", "Narwhal",
    "Needlefish", "Newt", "Nighthawk", "Nightingale", "Numbat", "Ocelot", "Octopus", "Okapi",
    "Olaf", "Olingo", "Opossum", "Orangutan",
    "Orca", "Oribi", "Ostrich", "Otter", "Owl", "Ox", "Panda", "Panther", "Parakeet", "Parrot",
    "Parrotfish", "Partridge",
    "Peacock", "Peafowl", "Pelican", "Penguin", "Perch", "Pheasant", "Pig", "Pike", "Pinniped",
    "Piranha", "Planarian",
    "Platypus", "Pony", "Porcupine", "Porpoise", "Possum", "Prawn", "Primate", "Ptarmigan",
    "Puffin", "Puma", "Python",
    "Quail", "Quelea", "Quetzal", "Quokka", "Raccoon", "Rat", "Rattlesnake", "Raven", "Reindeer",
    "Reptile", "Rhinoceros",
    "Roadrunner", "Rodent", "Rook", "Rooster", "Roundworm", "Sailfish", "Salamander", "Salmon",
    "Sawfish", "Scallop",
    "Scorpion", "Seahorse", "Serval", "Shrimp", "Silkworm", "Silverfish", "Skink", "Skunk", "Sloth",
    "Slug", "Smelt",
    "Snail", "Snipe", "Sole", "Sparrow", "Spider", "Spoonbill", "Squid", "Squirrel", "Starfish",
    "Stingray", "Stoat", "Stork",
    "Sturgeon", "Swallow", "Swan", "Swift", "Swordfish", "Swordtail", "Tahr", "Takin", "Tapir",
    "Tarantula", "Tarsier",
    "Termite", "Tern", "Tick", "Tiger", "Tiglon", "Titi", "Toad", "Tortoise", "Toucan", "Trout",
    "Tuna", "Turtle",
    "Tyrannosaurus", "Unicorn", "Urial", "Vaquita", "Viper", "Voalavoanala", "Vole", "Vulture",
    "Wallaby", "Walrus",
    "Warbler", "Wasp", "Waterbuck", "Weasel", "Whale", "Whippet", "Whitefish", "Wildcat",
    "Wildebeest", "Wildfowl", "Wolf",
    "Wolverine", "Wombat", "Woodchuck", "Woodpecker", "Worm", "Wren", "Xerinae", "Yak", "Zebra",
    "Zebu", "Zorilla",
    "Alfalfa", "Allium", "Alyssum", "Amaranth", "Anemone", "Anise", "Apple", "Apricot", "Artemisia",
    "Artichoke", "Arugula",
    "Asparagus", "Aster", "Astilbe", "Aubergine", "Avocado", "Azuki", "Banana", "Basil", "Bean",
    "Beet", "Beetroot",
    "Bellflower", "Blackberry", "Blackcurrant", "Blanketflower", "Blueberry", "Bougainvillea",
    "Boysenberry", "Broccoli",
    "Broom", "Cabbage", "Camellia", "Caraway", "Carrot", "Catmint", "Cauliflower", "Celeriac",
    "Celery", "Chamomile", "Chard",
    "Cheddar", "Cherry", "Chickpea", "Chives", "Chrysanthemum", "Cilantro", "Clematis", "Coconut",
    "Columbine", "Coneflower",
    "Coreopsis", "Coriander", "Cosmos", "Courgette", "Crocus", "Cucumber", "Cyclamen", "Dahlia",
    "Daikon", "Delicata", "Delphinium",
    "Dill", "Eggplant", "Endive", "Fennel", "Fig", "Foxglove", "Frisee", "Garlic", "Geranium",
    "Ginger", "Gladiolus",
    "Globeflower", "Grape", "Grapefruit", "Habanero", "Hollyhock", "Honeysuckle", "Hosta",
    "Hyacinth", "Hydrangea", "Impatien",
    "Iris", "Jicama", "Kale", "Kerria", "Kiwi", "Kohlrabi", "Lamium", "Lantana", "Larkspur",
    "Lavender", "Leek", "Lemon",
    "Lemongrass", "Lentil", "Lettuce", "Lilac", "Lime", "Lobelia", "Loosestrife", "Lupine",
    "Lychee", "Mandarin", "Mangetout",
    "Mango", "Marigold", "Marjoram", "Marrow", "Melon", "Mushroom", "Narcissus", "Nasturtium",
    "Nectarine", "Nicotiana", "Okra",
    "Oleander", "Onion", "Onions", "Orange", "Oregano", "Pansy", "Papaya", "Paprika", "Parrot",
    "Parsley", "Parsnip", "Passion",
    "Pea", "Peach", "Pear", "Peony", "Pepper", "Petunia", "Pineapple", "Plum", "Poppy", "Potato",
    "Primrose", "Pumpkin",
    "Quandong", "Quince", "Radicchio", "Radish", "Raspberry", "Rhododendron", "Rhubarb", "Rosemary",
    "Rutabaga", "Sage", "Salsify",
    "Salvia", "Scabiosa", "Scallion", "Scilla", "Sedum", "Shallot", "Skirret", "Snowdrops",
    "Spinach", "Sprout", "Squash",
    "Strawberry", "Sunchokes", "Sweetcorn", "Taro", "Thyme", "Tomato", "Topinambur", "Tubers",
    "Tulip", "Turnip", "Vinca",
    "Wasabi", "Watercress", "Watermelon", "Wisteria", "Yam", "Yarrow", "Zucchini"]


def _generate_name():
    while True:
        name = random.choice(adjectives)+random.choice(nouns)
        if len(name) <= 15:
            return name


def shallow_command_analysis(command):
    i = 0
    xx = 'xx'
    yy = 'yy'
    parent_task = None
    while i < len(command):
        if (command[i] == '-m' or command[i] == '--model') and i+1 < len(command):
            parent_task = command[i+1]
            i += 1
        elif (command[i] == '-c' or command[i] == '--config') and i+1 < len(command):
            config = json.loads(command[i+1])
            if not parent_task and "model" in config:
                parent_task = config["model"]
            if "source" in config:
                xx = config["source"]
            if "target" in config:
                yy = config["target"]
            i += 1
        i += 1
    return (xx+yy, parent_task)


def change_parent_task(command, task_id):
    i = 0
    while i < len(command):
        if (command[i] == '-m' or command[i] == '--model') and i+1 < len(command):
            command[i+1] = task_id
            return
        i += 1
    command.insert(0, task_id)
    command.insert(0, '-m')


def remove_config_option(command):
    i = 0
    while i < len(command):
        if (command[i] == '-c' or command[i] == '--config') and i+1 < len(command):
            del command[i:i+2]
            return
        i += 1


model_types = [
    "trans",
    "train",
    "preprocess",
    "vocab",
    "release"
]
model_type_map = {t[0:5]: t for t in model_types}


def model_name_analysis(model):
    task_type = None
    struct = {}
    lst = model.split("_")
    if lst[-1] in model_types:
        task_type = lst[-1][:5]
        lst.pop(-1)
    else:
        task_type = "train"
    if len(lst) < 4 or len(lst) > 5:
        return None, None
    struct["trid"] = lst.pop(0)
    struct["xxyy"] = lst.pop(0)
    struct["name"] = lst.pop(0)
    struct["nn"] = lst.pop(0)
    try:
        int(struct["nn"])
    except ValueError:
        if len(lst) == 0:
            lst.append(struct["nn"])
            del struct["nn"]
    uuid = lst.pop(0)
    usplit = uuid.split('-')
    if len(usplit) > 1:
        struct["uuid"] = usplit[0]
        struct["parent_uuid"] = usplit[-1]
    else:
        struct["uuid"] = uuid
    return struct, task_type


def build_task_id(content, xxyy, task_type, parent_task):
    # let us build a meaningful name for the task
    # name will be TRID_XXYY_NAME_NN_UUID(:UUID)-TYPE with:
    # * TRID - the trainer ID
    # * XXYY - the language pair
    # * NAME - user provided or generated name
    # * NN - the iteration (epoch) - automatically incremented for training task
    # * UUID - one or 2 parts - parent:child or child
    # * TYPE - trans|prepr|vocab|relea or other 5 letter action

    # first find nature of the task - train or not
    is_train = task_type == "train"
    is_buildvocab = task_type == "vocab"
    trid = 'XXXX'
    if 'trainer_id' in content and content['trainer_id']:
        trid = content['trainer_id']

    name = content["name"] if "name" in content else None
    parent_uuid = ''
    nn = None
    parent_task_type = None
    if parent_task is not None:
        struct_name, parent_task_type = model_name_analysis(parent_task)
        if name is None and "name" in struct_name:
            name = struct_name["name"]
        if (xxyy is None or xxyy == 'xxyy') and "xxyy" in struct_name:
            xxyy = struct_name["xxyy"]
        if "uuid" in struct_name:
            parent_uuid = '-'+struct_name["uuid"][0:5]
        if "nn" in struct_name:
            nn = int(struct_name["nn"])

    if nn is None:
        if is_buildvocab:
            nn = 0
        else:
            nn = 1
    else:
        if task_type == "prepr" or (task_type == "train" and parent_task_type != "prepr"):
            nn += 1

    if not name:
        name = _generate_name()

    the_uuid = str(uuid.uuid4()).replace("-", "")

    if nn is None:
        task_id = '%s_%s_%s_%s' % (trid, xxyy, name, the_uuid)
    else:
        task_id = '%s_%s_%s_%02d_%s' % (trid, xxyy, name, nn, the_uuid)
    task_id = task_id[0:47-len(parent_uuid)] + parent_uuid
    if task_type != "train":
        task_id += '_' + model_type_map[task_type]
    return task_id


def boolean_param(value):
    return not(value is None or
               value is False or
               value == "" or
               value == "0" or
               value == "False")
