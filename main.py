import logging
import random


logging.basicConfig(
    level=logging.DEBUG,
    filename='testlog.log',
    filemode='w',
    format='%(message)s'
)


class House:
    def __init__(self):
        self.mess = 0
        self.food = 0


class Pet:
    pet_list = {
        'Dog': {'feed': 50, 'active': 20, 'rarity': 7},
        'Cat': {'feed': 60, 'active': 10, 'rarity': 30},
        'Parrot': {'feed': 70, 'active': 15, 'rarity': 18},
        'Snake': {'feed': 80, 'active': 17, 'rarity': 14},
    }

    def __init__(self):
        self.pet = random.choice(list(Auto.pet_list))
        self.feed = Auto.pet_list[self.pet]['feed']
        self.active = Auto.pet_list[self.pet]['active']
        self.rarity = Auto.pet_list[self.pet]['rarity']


class Auto:
    car_list = {
        'BMW': {'fuel': 100, 'durability': 100, 'consumption': 6},
        'ZAZ': {'fuel': 50, 'durability': 40, 'consumption': 10},
        'Volvo': {'fuel': 70, 'durability': 150, 'consumption': 8},
        'Ferrari': {'fuel': 80, 'durability': 120, 'consumption': 14},
    }

    def __init__(self):
        self.brand = random.choice(list(Auto.car_list))
        self.fuel = Auto.car_list[self.brand]['fuel']
        self.durability = Auto.car_list[self.brand]['durability']
        self.consumption = Auto.car_list[self.brand]['consumption']

    def drive(self):
        if self.durability > 0 and self.fuel >= self.consumption:
            logging.debug('Driving...')
            self.fuel -= self.consumption
            self.durability -= 1
            return True
        else:
            logging.debug('This car cant go!')
            return False


class Job:
    job_list = {
        'Python developer': {'salary': 40, 'sadness': 3},
        'Java developer': {'salary': 50, 'sadness': 10},
        'C++ developer': {'salary': 45, 'sadness': 25},
        'Rust developer': {'salary': 70, 'sadness': 1},
    }

    def __init__(self):
        self.job_title = random.choice(list(Job.job_list))
        self.salary = Job.job_list[self.job_title]['salary']
        self.sadness = Job.job_list[self.job_title]['sadness']


class Human:
    def __init__(
            self,
            name='Human',
            job=None,
            home=None,
            car=None,
            pet=None
    ):
        self.name = name
        self.money = 100
        self.happiness = 50
        self.satiety = 50
        self.job = job
        self.car = car
        self.home = home
        self.pet = pet

    def get_home(self):
        self.home = House()

    def get_pet(self):
        self.pet = Pet()

    def get_car(self):
        self.car = Auto()

    def get_job(self):
        if self.car.drive():
            self.job = Job()
        else:
            self.to_repair()

    def to_repair(self):
        self.car.durability += 100
        self.money -= 50

    def eat(self):
        if self.home.food <= 0:
            self.shopping('food')
        else:
            if self.satiety >= 100:
                self.satiety = 100
            else:
                self.satiety += 5
                self.home.food -= 5

    def shopping(self, goal):
        if self.car.drive():
            pass
        else:
            if self.car.fuel < self.car.consumption:
                goal = 'fuel'
            else:
                self.to_repair()
                return
        if goal == 'fuel':
            logging.debug('I bought fuel')
            self.money -= 100
            self.car.fuel += 100
        elif goal == 'food':
            logging.debug('I bought food')
            self.money -= 50
            self.home.food += 50
        elif goal == 'sweets':
            logging.debug('I bought sweets!!!')
            self.money -= 15
            self.satiety += 2
            self.happiness += 10

    def work(self):
        if self.car.drive():
            pass
        else:
            if self.car.fuel < self.car.consumption:
                self.shopping('fuel')
                return
            else:
                self.to_repair()
                return
        self.money += self.job.salary
        self.happiness -= self.job.sadness
        self.satiety -= 4

    def chill(self):
        self.happiness += 10
        self.home.mess += 5

    def clean_home(self):
        self.happiness -= 5
        self.home.mess = 0

    def status(self, day):
        day_str = f'Today the {day} day of {self.name}\'s life'
        logging.debug(f'{day_str:=^50}')
        logging.debug('\n')
        human_info = f'{self.name}\'s info'
        logging.debug(f'{human_info:^50}')
        logging.debug('\n')
        logging.debug(f'money: {self.money}')
        logging.debug(f'satiety: {self.satiety}')
        logging.debug(f'happiness: {self.happiness}')
        home_info = 'Home info'
        logging.debug(f'{home_info:^50}')
        logging.debug('\n')
        logging.debug(f'mess: {self.home.mess}')
        logging.debug(f'food: {self.home.food}')
        car_info = f'{self.car.brand} car info'
        logging.debug(f'{car_info:^50}')
        logging.debug('\n')
        logging.debug(f'fuel: {self.car.fuel}')
        logging.debug(f'durability: {self.car.durability}')

    def is_alive(self):
        if self.happiness < 0:
            logging.debug('Depression...')
            return False
        elif self.satiety < 0:
            logging.debug('Dead...')
            return False
        elif self.money < -500:
            logging.debug('Bankrupt')
            return False
        else:
            return True

    def live_a_day(self, day):
        if not self.is_alive():
            return False
        if self.home is None:
            logging.debug('Settled in the house')
            self.get_home()
        if self.car is None:
            self.get_car()
            logging.debug(f'I bought a car {self.car.brand}')
        if self.job is None:
            self.get_job()
            logging.debug(f'I got a job {self.job.job_title} with salary {self.job.salary}')
        self.status(day)
        dice = random.randint(1, 4)
        if self.satiety < 20:
            logging.debug('Ill go to eat')
            self.eat()
        elif self.happiness < 20:
            if self.home.mess <= 15:
                logging.debug('Lets chill')
                self.chill()
            else:
                logging.debug('I need to clean')
                self.clean_home()
        elif self.money < 0:
            logging.debug('Start working')
            self.work()
        elif self.car.durability < 15:
            logging.debug('I need to repair my car')
            self.to_repair()
        elif dice == 1:
            logging.debug('Lets chill')
            self.chill()
        elif dice == 2:
            logging.debug('Start working')
            self.work()
        elif dice == 3:
            logging.debug('I need to clean')
            self.clean_home()
        elif dice == 4:
            logging.debug('Time for sweets!')
            self.shopping('sweets')
        return True


nick = Human('Nick')
for day in range(1, 8):
    if not nick.live_a_day(day):
        break

logging.debug(f'x = {nick.live_a_day}')
logging.info('You are using Python3')
logging.warning('This method will be deprecated in the next update!')
logging.error('Error!')
logging.critical('FATAL ERROR!')
logging.shutdown()
