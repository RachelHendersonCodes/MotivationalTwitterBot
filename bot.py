import tweepy
from random import randint
from datetime import datetime
import time
from Subscribed_Users import SubscribedUsers
import json


with open('BotConfigs.json', 'r') as bot_configs:
    config_data = json.load(bot_configs)
    consumer_key = config_data[0]["consumer_key"] # apikey
    consumer_secret = config_data[0]["consumer_secret"] # apisecretkey
    key = config_data[0]["key"] # accesstoken
    secret = config_data[0]["secret"] # accesstokensecret

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(key, secret)

api = tweepy.API(auth)

day_of_week = datetime.today().weekday()
day_of_year = datetime.today().timetuple().tm_yday

subscribed_list = []
subscribed_user = ""
users_tweeted = []
remove_users = []
users_tfs = []
response_counter = 0


def read_sent_daily_tweet():
    file_read = open('last_day_sent.txt', 'r')
    last_sent_tweet = file_read.read().strip()
    file_read.close()
    return last_sent_tweet

# prevents duplicate tweet error
def store_sent_daily_tweet(last_sent_tweet):
    # file_read = file_read + "\n"
    file_write = open('last_day_sent.txt', 'w')
    last_sent_tweet = str(last_sent_tweet)
    file_write.write(last_sent_tweet)
    file_write.close()
    return


last_daily_tweet_sent = read_sent_daily_tweet()


def daily_tweet():
    if datetime.today().weekday() == 0:
        hashtag = "#MondayMotivation"
    else:
        hashtag = "#Motivation"
    if day_of_year == 174:
        tweet_to_publish = "What are you doing this morning to make sure you have the best week you can? Let me know how I can help! I believe in you! " + hashtag
        media = api.media_upload("project_images/174.png")
        post_result = api.update_status(status=tweet_to_publish, media_ids=[media.media_id])
        store_sent_daily_tweet(day_of_year)
        print(post_result)
    elif day_of_year == 175:
        tweet_to_publish = "If you want to win in the end, and I mean truly win, you must remember to always stay true to yourself " + hashtag
        media = api.media_upload("project_images/175.png")
        post_result = api.update_status(status=tweet_to_publish, media_ids=[media.media_id])
        print(post_result)
    elif day_of_year == 176:
        tweet_to_publish = "Getting comfortable with discomfort is your ticket to your dream life " + hashtag
        media = api.media_upload("project_images/176.png")
        post_result = api.update_status(status=tweet_to_publish, media_ids=[media.media_id])
        print(post_result)
    elif day_of_year == 177:
        tweet_to_publish = "Self-care is a necessary part of any successful person's routine " + hashtag
        media = api.media_upload("project_images/177.png")
        post_result = api.update_status(status=tweet_to_publish, media_ids=[media.media_id])
        print(post_result)
    elif day_of_year == 178:
        tweet_to_publish = "The limits others think we hold are not our limits. " + hashtag
        media = api.media_upload("project_images/178.png")
        post_result = api.update_status(status=tweet_to_publish, media_ids=[media.media_id])
        print(post_result)
    elif day_of_year == 179:
        tweet_to_publish = "Happy Saturday! " + hashtag
        media = api.media_upload("project_images/179.png")
        post_result = api.update_status(status=tweet_to_publish, media_ids=[media.media_id])
        print(post_result)
    elif day_of_year == 181:
        tweet_to_publish = "Get Monday started off on the right foot by entering your week with a grateful mind! " + hashtag
        media = api.media_upload("project_images/181.png")
        post_result = api.update_status(status=tweet_to_publish, media_ids=[media.media_id])
        print(post_result)
    elif day_of_year == 219:
        tweet_to_publish = "When it comes to overcoming challenges, mindset is half the battle. Ground yourself in " \
                           "gratitude " + hashtag
        media = api.media_upload("project_images/219.png")
        post_result = api.update_status(status=tweet_to_publish, media_ids=[media.media_id])
        print(post_result)
    elif day_of_year == 225:
        tweet_to_publish = "The way to get started is to quit talking and begin doing. - Walt Disney"
        post_result = api.update_status(status=tweet_to_publish)
        print(post_result)
    elif day_of_year == 229:
        tweet_to_publish = "Whatever you are, be a good one. ― Abraham Lincoln"
        post_result = api.update_status(status=tweet_to_publish)
        print(post_result)
    elif day_of_year == 230:
        tweet_to_publish = "You can either experience the pain of discipline or the pain of regret. The choice is yours."
        post_result = api.update_status(status=tweet_to_publish)
        store_sent_daily_tweet(day_of_year)
        print(post_result)
    elif day_of_year == 231:
        tweet_to_publish = "“Some people want it to happen, some wish it would happen, others make it happen.” – Michael Jordan"
        post_result = api.update_status(status=tweet_to_publish)
        store_sent_daily_tweet(day_of_year)
        print(post_result)
    elif day_of_year == 232:
        tweet_to_publish = "“If opportunity doesn’t knock, build a door.” – Kurt Cobain"
        post_result = api.update_status(status=tweet_to_publish)
        store_sent_daily_tweet(day_of_year)
        print(post_result)
    elif day_of_year == 233:
        tweet_to_publish = "“Never give up on a dream just because of the time it will take to accomplish it. The time will pass anyway.” – Earl Nightingale"
        post_result = api.update_status(status=tweet_to_publish)
        store_sent_daily_tweet(day_of_year)
        print(post_result)
    elif day_of_year == 236:
        tweet_to_publish = "\"Things work out best for those who make the best of how things work out.\" -John Wooden"
        post_result = api.update_status(status=tweet_to_publish)
        store_sent_daily_tweet(day_of_year)
        print(post_result)
    elif day_of_year == 237:
        tweet_to_publish = "\"Success is walking from failure to failure with no loss of enthusiasm.\" -Winston Churchill"
        post_result = api.update_status(status=tweet_to_publish)
        store_sent_daily_tweet(day_of_year)
        print(post_result)
    elif day_of_year == 238:
        tweet_to_publish = "\"Just when the caterpillar thought the world was ending, he turned into a butterfly.\" -Proverb"
        post_result = api.update_status(status=tweet_to_publish)
        store_sent_daily_tweet(day_of_year)
        print(post_result)
    elif day_of_year == 239:
        tweet_to_publish = "\"Whenever you see a successful person you only see the public glories, never the private sacrifices to reach them.\" -Vaibhav Shah"
        post_result = api.update_status(status=tweet_to_publish)
        store_sent_daily_tweet(day_of_year)
        print(post_result)
    elif day_of_year == 240:
        tweet_to_publish = "\"Try not to become a person of success, but rather try to become a person of value.\" -Albert Einstein"
        post_result = api.update_status(status=tweet_to_publish)
        store_sent_daily_tweet(day_of_year)
        print(post_result)
    elif day_of_year == 241:
        tweet_to_publish = "\"I have not failed. I've just found 10,000 ways that won't work.\" -Thomas A. Edison"
        post_result = api.update_status(status=tweet_to_publish)
        store_sent_daily_tweet(day_of_year)
        print(post_result)
    elif day_of_year == 242:
        tweet_to_publish = "\"A successful man is one who can lay a firm foundation with the bricks others have thrown at him.\" -David Brinkley"
        post_result = api.update_status(status=tweet_to_publish)
        store_sent_daily_tweet(day_of_year)
        print(post_result)
    elif day_of_year == 243:
        tweet_to_publish = "\"The meaning of life is to find your gift. The purpose of life is to give it away.\" -Anonymous"
        post_result = api.update_status(status=tweet_to_publish)
        store_sent_daily_tweet(day_of_year)
        print(post_result)
    elif day_of_year == 244:
        tweet_to_publish = "\"Happiness is a butterfly, which when pursued, is always beyond your grasp, but which, if you will sit down quietly, may alight upon you.\" -Nathaniel Hawthorne"
        post_result = api.update_status(status=tweet_to_publish)
        store_sent_daily_tweet(day_of_year)
        print(post_result)
    elif day_of_year == 245:
        tweet_to_publish = "\"Life is not about finding yourself. Life is about creating yourself.\" -Lolly Daskal"
        post_result = api.update_status(status=tweet_to_publish)
        store_sent_daily_tweet(day_of_year)
        print(post_result)
    elif day_of_year == 246:
        tweet_to_publish = "\"Your problem isn't the problem. Your reaction is the problem.\" -Anonymous"
        post_result = api.update_status(status=tweet_to_publish)
        store_sent_daily_tweet(day_of_year)
        print(post_result)
    elif day_of_year == 247:
        tweet_to_publish = "\"There are two types of people who will tell you that you cannot make a difference in " \
                           "this world: those who are afraid to try and those who are afraid you will succeed.\" -Ray" \
                           " Goforth "
        post_result = api.update_status(status=tweet_to_publish)
        store_sent_daily_tweet(day_of_year)
        print(post_result)
    elif day_of_year == 248:
        tweet_to_publish = "\"Thinking should become your capital asset, no matter whatever ups and downs you come across in your life.\" -A.P.J. Abdul Kalam"
        post_result = api.update_status(status=tweet_to_publish)
        store_sent_daily_tweet(day_of_year)
        print(post_result)
    elif day_of_year == 249:
        tweet_to_publish = "\"Success is the sum of small efforts, repeated day-in and day-out.\" -Robert Collier"
        post_result = api.update_status(status=tweet_to_publish)
        store_sent_daily_tweet(day_of_year)
        print(post_result)
    elif day_of_year == 250:
        tweet_to_publish = "\"All progress takes place outside the comfort zone.\" -Michael John Bobak"
        post_result = api.update_status(status=tweet_to_publish)
        store_sent_daily_tweet(day_of_year)
        print(post_result)
    elif day_of_year == 251:
        tweet_to_publish = "\"You may only succeed if you desire succeeding; you may only fail if you do not mind failing.\" -Philippos"
        post_result = api.update_status(status=tweet_to_publish)
        store_sent_daily_tweet(day_of_year)
        print(post_result)
    elif day_of_year == 252:
        tweet_to_publish = "\"People often say that motivation doesn't last. Well, neither does bathing--that's why we recommend it daily.\" -Zig Ziglar"
        post_result = api.update_status(status=tweet_to_publish)
        store_sent_daily_tweet(day_of_year)
        print(post_result)
    elif day_of_year == 253:
        tweet_to_publish = "\"The only place where success comes before work is in the dictionary.\" -Vidal Sassoon"
        post_result = api.update_status(status=tweet_to_publish)
        store_sent_daily_tweet(day_of_year)
        print(post_result)
    elif day_of_year == 254:
        tweet_to_publish = "\"As we look ahead into the next century, leaders will be those who empower others.\" -Bill Gates"
        post_result = api.update_status(status=tweet_to_publish)
        store_sent_daily_tweet(day_of_year)
        print(post_result)
    elif day_of_year == 255:
        tweet_to_publish = "\"The successful warrior is the average man, with laser-like focus.\" -Bruce Lee"
        post_result = api.update_status(status=tweet_to_publish)
        store_sent_daily_tweet(day_of_year)
        print(post_result)
    elif day_of_year == 256:
        tweet_to_publish = "\"When I dare to be powerful, to use my strength in the service of my vision, then it becomes less and less important whether I am afraid.\" --Audre Lorde"
        post_result = api.update_status(status=tweet_to_publish)
        store_sent_daily_tweet(day_of_year)
        print(post_result)
    elif day_of_year == 257:
        tweet_to_publish = "\"Develop success from failures. Discouragement and failure are two of the surest stepping stones to success.\" -Dale Carnegie"
        post_result = api.update_status(status=tweet_to_publish)
        store_sent_daily_tweet(day_of_year)
        print(post_result)
    elif day_of_year == 258:
        tweet_to_publish = "\"If you don't design your own life plan, chances are you'll fall into someone else's plan. And guess what they have planned for you? Not much.\" -Jim Rohn"
        post_result = api.update_status(status=tweet_to_publish)
        store_sent_daily_tweet(day_of_year)
        print(post_result)
    elif day_of_year == 259:
        tweet_to_publish = "\"I don't want to get to the end of my life and find that I lived just the length of it. I want to have lived the width of it as well.\" -Diane Ackerman"
        post_result = api.update_status(status=tweet_to_publish)
        store_sent_daily_tweet(day_of_year)
        print(post_result)
    elif day_of_year == 260:
        tweet_to_publish = "\"You must expect great things of yourself before you can do them.\" -Michael Jordan"
        post_result = api.update_status(status=tweet_to_publish)
        store_sent_daily_tweet(day_of_year)
        print(post_result)
    elif day_of_year == 261:
        tweet_to_publish = "\"Be miserable. Or motivate yourself. Whatever has to be done, it's always your choice.\" -Wayne Dyer"
        post_result = api.update_status(status=tweet_to_publish)
        store_sent_daily_tweet(day_of_year)
        print(post_result)
    elif day_of_year == 262:
        tweet_to_publish = "\"What would you do if you weren't afraid?\""
        post_result = api.update_status(status=tweet_to_publish)
        store_sent_daily_tweet(day_of_year)
        print(post_result)
    elif day_of_year == 263:
        tweet_to_publish = "\"If you believe in yourself and have the courage, the determination, the dedication, " \
                           "the competitive drive and if you are willing to sacrifice the little things in life and " \
                           "pay the price for the things that are worthwhile, it can be done.\" --Vince Lombardi "
        post_result = api.update_status(status=tweet_to_publish)
        store_sent_daily_tweet(day_of_year)
        print(post_result)
    elif day_of_year == 265:
        tweet_to_publish = "\"Don't downgrade your dream just to fit your reality. Upgrade your conviction to match your destiny.\" ― Stuart Scott "
        post_result = api.update_status(status=tweet_to_publish)
        store_sent_daily_tweet(day_of_year)
        print(post_result)
    elif day_of_year == 266:
        tweet_to_publish = "\"What you get by achieving your goals is not as important as what you become by achieving your goals.\" - Zig Ziglar "
        post_result = api.update_status(status=tweet_to_publish)
        store_sent_daily_tweet(day_of_year)
        print(post_result)
    elif day_of_year == 268:
        tweet_to_publish = "\"No matter what people tell you, words and ideas can change the world.\" – Robin Williams"
        post_result = api.update_status(status=tweet_to_publish)
        store_sent_daily_tweet(day_of_year)
        print(post_result)
    elif day_of_year == 269:
        tweet_to_publish = "\"Only I can change my life. No one can do it for me.\" – Carol Burnett"
        post_result = api.update_status(status=tweet_to_publish)
        store_sent_daily_tweet(day_of_year)
        print(post_result)
    elif day_of_year == 270:
        tweet_to_publish = "\"The clock is ticking. Are you becoming the person you want to be?’ — Greg Plitt\""
        post_result = api.update_status(status=tweet_to_publish)
        store_sent_daily_tweet(day_of_year)
        print(post_result)
    elif day_of_year == 271:
        tweet_to_publish = "\"Opportunity does not knock, it presents itself when you beat down the door.\" – Kyle Chandler"
        post_result = api.update_status(status=tweet_to_publish)
        store_sent_daily_tweet(day_of_year)
        print(post_result)
    elif day_of_year == 272:
        tweet_to_publish = "\"I never lose. Either I win or learn.\" – Nelson Mandela"
        post_result = api.update_status(status=tweet_to_publish)
        store_sent_daily_tweet(day_of_year)
        print(post_result)
    elif day_of_year == 273:
        tweet_to_publish = "\"Sunshine all the time makes a desert.\" – Arabic Proverb"
        post_result = api.update_status(status=tweet_to_publish)
        store_sent_daily_tweet(day_of_year)
        print(post_result)
    elif day_of_year == 274:
        tweet_to_publish = "\"Nothing can dim the light that shines from within.\" – Maya Angelou"
        post_result = api.update_status(status=tweet_to_publish)
        store_sent_daily_tweet(day_of_year)
        print(post_result)
    elif day_of_year == 275:
        tweet_to_publish = "\"This is a reminder to you to create your own rule book, and live your life the way you want it.\" – Reese Evans"
        post_result = api.update_status(status=tweet_to_publish)
        store_sent_daily_tweet(day_of_year)
        print(post_result)
    elif day_of_year == 276:
        tweet_to_publish = "\"I choose to make the rest of my life, the best of my life.\" – Louise Hay"
        post_result = api.update_status(status=tweet_to_publish)
        store_sent_daily_tweet(day_of_year)
        print(post_result)
    elif day_of_year == 279:
        tweet_to_publish = "\"Take criticism seriously, but not personally. If there is truth or merit in the " \
                           "criticism, try to learn from it. Otherwise, let it roll right off you.\" – Hillary Clinton "
        post_result = api.update_status(status=tweet_to_publish)
        store_sent_daily_tweet(day_of_year)
        print(post_result)
    elif day_of_year == 280:
        tweet_to_publish = "\"Believe in yourself, take on your challenges, dig deep within yourself to conquer " \
                           "fears. Never let anyone bring you down. You got to keep going.\" – Chantal Sutherland "
        post_result = api.update_status(status=tweet_to_publish)
        store_sent_daily_tweet(day_of_year)
        print(post_result)
    elif day_of_year == 281:
        tweet_to_publish = "\"Yesterday I was clever, so I wanted to change the world. Today I am wise, so I am changing myself.\" – Rumi"
        post_result = api.update_status(status=tweet_to_publish)
        store_sent_daily_tweet(day_of_year)
        print(post_result)
    elif day_of_year == 282:
        tweet_to_publish = "\"If you can’t do anything about it then let it go. Don’t be a prisoner to things you " \
                           "can’t change.\" – Tony Gaskins "
        post_result = api.update_status(status=tweet_to_publish)
        store_sent_daily_tweet(day_of_year)
        print(post_result)
    elif day_of_year == 284:
        tweet_to_publish = "\"Life is 10% what happens to you and 90% how you react to it.\" - Charles R. Swindoll "
        post_result = api.update_status(status=tweet_to_publish)
        store_sent_daily_tweet(day_of_year)
        print(post_result)
    elif day_of_year == 287:
        tweet_to_publish = "\"Success is no accident. It is hard work, perseverance, learning, studying, sacrifice and most of all, love of what you are doing or learning to do\"  ― Pele"
        post_result = api.update_status(status=tweet_to_publish)
        store_sent_daily_tweet(day_of_year)
        print(post_result)
    elif day_of_year == 288:
        tweet_to_publish = "\"The same boiling water that softens the potato hardens the egg. It’s what you’re made of. Not the circumstances.\" – Unknown"
        post_result = api.update_status(status=tweet_to_publish)
        store_sent_daily_tweet(day_of_year)
        print(post_result)
    elif day_of_year == 294:
        tweet_to_publish = "\"It is better to fail in originality than to succeed in imitation.\" -Herman Melville"
        post_result = api.update_status(status=tweet_to_publish)
        store_sent_daily_tweet(day_of_year)
        print(post_result)







def read_last_seen():
    file_read = open('last_seen.txt', 'r')
    last_seen_id = file_read.read().strip()
    file_read.close()
    return last_seen_id


# stores tweet id of tweet being responded to when called
def store_last_seen(last_seen_id):
    # file_read = file_read + "\n"
    file_write = open('last_seen.txt', 'w')
    last_seen_id = str(last_seen_id)
    file_write.write(last_seen_id)
    file_write.close()
    return


def read_users():
    file_read = open('OptIn.txt', 'r')
    stored_username = file_read.read()
    file_read.close()
    return stored_username


# stores usernames of users who will receive weekly tweets
def store_users(stored_username):
    file_write = open('OptIn.txt', 'a')
    file_write.write(str('\n' + stored_username))
    file_write.close()
    return


# will remove any empty lines left in OptIn.txt when users opt out
def remove_empty_lines():
    with open('OptIn.txt') as optin:
        opt_lines = optin.readlines()
    with open('OptIn.txt', 'w') as optin:
        opt_lines = filter(str.strip, opt_lines)
        optin.writelines(opt_lines)


def read_tip_count():
    file_read = open('tip_count.txt', 'r')
    stored_tip_count = file_read.read()
    file_read.close()
    return stored_tip_count


def store_tip_count(stored_tip_count):
    file_write = open('tip_count.txt', 'w')
    file_write.write(stored_tip_count)
    file_write.close()
    return


def stored_tips(set_username):
    tweet_count = int(read_tip_count())
    tip = ""
    media = ""
    at_username = "@" + set_username
    if tweet_count == 6:
        media = api.media_upload("project_images/tip_1.png")
        tip = "#ProductivityTip Time Blocking works because it encourages single-tasking & focus to achieve more so " \
              "you feel less stressed. The key is scheduling down time & " \
              "commutes, too! Helpful video to get started: https://www.youtube.com/watch?v=Y-aFEA0MCQ4 "
    elif tweet_count == 1:
        media = api.media_upload("project_images/tip_2.png")
        tip = "#ProductivityTip A simple change you can make this week to boost productivity: SAY NO! Stop trying to " \
              "please everyone & start using your time for YOUR priorities. It's okay to politely decline other's " \
              "requests so you can focus on your goals, passions, & dreams. "
    elif tweet_count == 2:
        media = api.media_upload("project_images/tip_3.png")
        tip = "#ProductivityTip Technology is great! BUT you must keep tabs on how many hours you pour into consuming " \
              "it in order to be productive, happy, & healthy. Stay connected w/ others online; but limit screen time " \
              "to ALSO be connected with yourself & your goals! "
    elif tweet_count == 3:
        tip = "And finally this"
    send_result = api.update_status(status=at_username + " " + tip, media_ids=[media.media_id])
    return send_result



def read_users_tfs():
    file_read = open("Users_TFS.txt", 'r')
    users_tweeted_from_search = file_read.read()
    file_read.close()
    return users_tweeted_from_search


def store_users_tfs(users_tweeted_from_search):
    file_write = open('Users_TFS.txt', 'a')
    file_write.write(str('\n' + users_tweeted_from_search))
    file_write.close()
    return


def physical_motivational_response():
    random_number = randint(0, 3)
    reply = ''
    if random_number == 0:
        reply = " The hardest part is starting. Lace those shoes up, then see how you feel. "
    elif random_number == 1:
        reply = " You CAN do it but first you have to go for it! You'll feel so much better once you get it done. I'm " \
                "rooting for you! "
    elif random_number == 2:
        reply = " You know what sounds fun right now? Getting that feeling when you hear your favorite song come on " \
                "the workout playlist. " \
                "Spend some time with yourself. Even if it's just 10 minutes. You won't regret it "
    elif random_number == 3:
        reply = " All the motivation you need is already inside of you. You set this goal for yourself because you " \
                "know you deserve to feel your best. Don't stop now. You got this "
    elif random_number == 4:
        reply = " You are seeing this tweet because the universe wants you to achieve your goals! Go for it! "
    return reply


def edu_motivational_response():
    random_number = randint(1, 6)
    reply = ''
    if random_number == 0:
        reply = " Imagine how good you'll feel once you get it done. You deserve that good feeling, rather" \
                "than it hanging over your head all day. Start chipping away at it now! "
    elif random_number == 1:
        reply = " You're so smart. The work you put in today will be another step to getting to that next level " \
                "you're capable of! You got this. "
    elif random_number == 2:
        reply = " Your future self will either be thanking you for getting started now " \
                " or stressed because you put it off. You deserve a calm mind. Choose " \
                "wisely "
    elif random_number == 3:
        reply = " I know it's hard, but... if anyone can do it, it's you. Education unlocks so many doors the world " \
                "needs you to open. Don't stop now. It'll feel so good when you get it done. I promise! "
    elif random_number == 4:
        reply = " Find the time to get it done because you deserve to see everything you're capable of " \
                "accomplishing. I know procrastination makes it seem hard, but procrastination doesn't have as " \
                "much power as it seems. You can do it! "
    elif random_number == 5:
        reply = " It can feel tough to get started. Try setting a 25 minute timer & try to focus on nothing but" \
                " your task until it goes off. Then you can take a 5 minute break if you feel you need one. " \
                " It'll feel good just knowing you've gotten started. I'm rooting for you! "
    elif random_number == 6:
        reply = " I really admire you for working so hard toward your education. This investment in your future will " \
                "pay off. I promise! "
    return reply


def tidy_motivational_response():
    random_number = randint(0, 2)
    reply = ''
    if random_number == 0:
        reply = " I believe in you! " + 'https://www.youtube.com/watch?v=s8hWQwFwayo'
    elif random_number == 1:
        reply = " You can do it! " + 'https://www.youtube.com/watch?v=FTociictyyE'
    elif random_number == 2:
        reply = "Your future self will either be grateful or stressed based on the decision present you makes. Choose " \
                "wisely "
    elif random_number == 3:
        reply = " "
    return reply


# def generic_motivational_response(): random_number = randint(0, 1) reply = '' if random_number == 0: reply = " I
# believe in you! " + 'https://www.youtube.com/watch?v=s8hWQwFwayo' elif random_number == 1: reply = " You can do it!
# " + 'https://www.youtube.com/watch?v=FTociictyyE' elif random_number == 2: reply = " Your future self will either
# be grateful or stressed based on the decision present you makes. Choose wisely " elif random_number == 3: reply = "
# " return reply
# Set search EQUAL TO value rather that searching if value is in the query

find_tweet = api.search(q="\"someone motivate me\"", since_id=read_last_seen(), count=40, show_user=True)
user_tweeted_from_search = read_users_tfs()
print(user_tweeted_from_search)


def send_motivation():
    for i in find_tweet:
        print(i.user.screen_name, i.text)
        print(i.text[0])
        print("RT" not in i.text)
        print("tw" not in i.text)
        if "gym" in i.text or "exercise" in i.text or "work out" in i.text or "workout" in i.text:
            if "kill" not in i.text and "die" not in i.text and "harm" not in i.text and "hurt" not in i.text and "kms" \
                    not in i.text and "suicide" not in i.text and "TW" not in i.text and "Trigger Warning" not in i.text and "self-harm" not in i.text and "RT" not in i.text:
                if i.user.screen_name not in user_tweeted_from_search:
                    api.update_status("@" + i.user.screen_name + physical_motivational_response(),
                                      in_reply_to_status_id=i.id)
                    print("@" + i.user.screen_name + physical_motivational_response())
                    store_users_tfs(i.user.screen_name)
                    users_tfs.append(i.user.screen_name)
                    # api.update_status
        elif "study" in i.text or "do homework" in i.text or "do hw" in i.text or "do my hw" in i.text or "school" in i.text or "essay" in i.text:
            if "kill" not in i.text and "die" not in i.text and "harm" not in i.text and "hurt" not in i.text and "kms" \
                    not in i.text and "suicide" not in i.text and "TW" not in i.text and "Trigger Warning" not in i.text and "self-harm" not in i.text and "RT" not in i.text:
                if i.user.screen_name not in user_tweeted_from_search:
                    api.update_status("@" + i.user.screen_name + edu_motivational_response(),
                                      in_reply_to_status_id=i.id)
                    store_users_tfs(i.user.screen_name)
                # api.update_status
        elif "tidy" in i.text or "organize" in i.text:
            if "kill" not in i.text or "die" not in i.text or "harm" not in i.text or "hurt" not in i.text or "kms" \
                    not in i.text or "suicide" not in i.text and "RT" not in i.text:
                if i.user.screen_name not in user_tweeted_from_search:
                    print("@" + i.user.screen_name + edu_motivational_response())
                    store_users_tfs(i.user.screen_name)
                    # api.update_status


def select_gif():
    random_number = randint(0, 5)
    selected_gif = ''
    if random_number == 0:
        selected_gif = api.media_upload("project_images/sponge_welcome.gif")
    elif random_number == 1:
        selected_gif = api.media_upload("project_images/seinfeld_welcome.gif")
    elif random_number == 2:
        selected_gif = api.media_upload("project_images/alice_welcome.gif")
    elif random_number == 3:
        selected_gif = api.media_upload("project_images/work_smarter.gif")
    elif random_number == 4:
        selected_gif = api.media_upload("project_images/yoda_welcome.gif")
    elif random_number == 5:
        selected_gif = api.media_upload("project_images/productive_penguin.gif")
    return selected_gif


gif = api.media_upload("project_images/sponge_welcome.gif")

stored_users = read_users()

while True:
    user_tweeted_from_search = read_users_tfs()
    send_motivation()
    print(day_of_year)
    print(day_of_week)
    read_sent_daily_tweet()
    last_daily_tweet_sent = read_sent_daily_tweet()
    if str(day_of_year) != last_daily_tweet_sent:
        daily_tweet()
        #store_sent_daily_tweet(day_of_year)
    tweets = api.mentions_timeline(read_last_seen(), tweet_mode='extended')
    gif = select_gif()

    for tweet in reversed(tweets):
        if '#GiveMeTips'.lower() in tweet.full_text.lower():
            print(str(tweet.id) + ' - ' + tweet.full_text)
            # print(tweet.user.screen_name not in Stored_Users)
            # print(read_users())
            if tweet.user.screen_name not in stored_users:
                api.update_status("@" + tweet.user.screen_name + " Thanks for signing up! You're helping me fulfill my "
                                                                 "purpose, which is helping you become everything "
                                                                 "you're meant to be! You will receive a maximum of 1 "
                                                                 "tweet per week in your mentions that will provide a "
                                                                 "helpful productivity tip you can implement in the "
                                                                 "week ahead! ", tweet.id, media_ids=[gif.media_id])
                store_last_seen(tweet.id)
                store_users(tweet.user.screen_name)
        elif '#StopProductivity'.lower() in tweet.full_text.lower():
            print(str(tweet.id) + ' - ' + tweet.full_text)
            if tweet.user.screen_name in stored_users:
                remove_users.append(tweet.user.screen_name)
                api.update_status("@" + tweet.user.screen_name + "You've opted out of receiving tips and will no "
                                                                 "longer receive mentions from this account. Thanks "
                                                                 "for giving it a chance! I hope I was able to give "
                                                                 "you some value. "
                                                                 "Wishing you all the best "
                                                                 "throughout life. I know you're going to do great. ", tweet.id)
                store_last_seen(tweet.id)
            elif tweet.user.screen_name not in stored_users:
                api.update_status("@" + tweet.user.screen_name + " I received an Opt-Out request but wasn't able to locate any "
                                                                 "Opt-In history from your account. Just confirming "
                                                                 "that you will not receive any mentions from me after this. You may "
                                                                 "choose to Opt-In at anytime. Wishing you all the best in reaching your goals. ", tweet.id)
                store_last_seen(tweet.id)



                # api.update_status("@" + tweet.user.screen_name + " You've been removed and will no longer receive tips. "
                # "Thank you! ")

    user_list = stored_users.split('\n')
    for names in remove_users:
        user_list.remove(names)
        with open('OptIn.txt', 'r') as fin:
            lines = fin.readlines()
        with open('OptIn.txt', 'w') as fout:
            for line in lines:
                for username in remove_users:
                    if line.strip('n') != username in remove_users:
                        fout.write(line)

    # updates text file with opted-out user removed
    remove_empty_lines()


    for username in user_list:
        subscribed_user = SubscribedUsers()
        subscribed_user.username = username
        subscribed_list.append(subscribed_user)

    tweet_count = int(read_tip_count())
    with open('last_day_tip_sent.txt', 'r') as last_day:
        last_tip_day = last_day.read()


    if day_of_week == 0:
        for user in subscribed_list:
            # if statement prevents re-execution after successful iteration
            if int(day_of_year) != int(last_tip_day):
                stored_tips(user.username)
                users_tweeted.append(user.username)
                print('Today is Sunday. I will send tips today.')
                print(tweet_count)
        # increments tips from stored_tips() after successful iteration so tip won't repeat next Sunday
        tweet_count += 1
        with open('last_day_tip_sent.txt', 'w') as overwrite_day:
            overwrite_day.write(str(day_of_year))


    # max stored tips have been reached, restarts the list of tips and sends from the beginning
    if tweet_count > 50:
        tweet_count = 1

    store_tip_count(str(tweet_count))

    time.sleep(10000)

# pause execution
# time.sleep()

# if user not in list:
#     tweet_to_send = "Thanks for signing up"

# WeeklyTipOptIn
# Send users a weekly productivity
# If user opts in, send first inital tweet to them welcoming them and congratulating them on deciding to become more produtive, explain
# ...that they will receive a weekly productivity tip every Sunday evening to get the next week started on the right foot
# Send productivity tip along with ways they can implement in [infograph?] [how it can be helpful]
# add ways to opt in and out in bio


# Tweet people who have the phrase "someone motivate me" in their tweet
# Send a maximum of 5 tweets in 4 hours [i'll need to keep a list of tweets already replied to]
# Gym
# Study
# Generic
# Embed videos with relevant motivational quote
