#/usr/bin/env python3

import random

import discord

import bisect

from dateutil import parser

# provided: read in the discord token
with open('discord_token.txt','r') as f:
    DISCORD_TOKEN = f.readline().strip()

# provided: variables
start_date = parser.parse('1/1/2021')
start_date_mahina_idx = 19 - 1
mahina_day_names = []
mahina_day_infos = []
special_days = []

#####################  TO DO #######################################
# word to wake up the bot
expected_activation_word = 'calendar'

# create a reply given message content and the sender of the message
def make_reply( msg_content,user_name):
    activation_len = len(expected_activation_word)
    activation_word = msg_content[:activation_len]
    task_word = msg_content[activation_len+1:]

    if activation_word != expected_activation_word:
        return ''
    
    if is_date(task_word):
        curr_idx = get_mahina_day_idx(task_word)
        curr_name = mahina_day_names[curr_idx]
        curr_info = mahina_day_infos[curr_idx]
        reply = task_word + ' is ' + curr_name + ': '+ curr_info
        
    else:
        reply = 'Aloha e ' + user_name + '!'
    return reply

# find mahina day
def get_mahina_day_idx(curr_date):
    curr_date = parser.parse(curr_date)
    num_sd_bef_start = 0
    num_sd_bef_curr = 0
    for special_day in special_days:
        if special_day <= start_date:
            num_sd_bef_start += 1
        if special_day <= curr_date:
            num_sd_bef_curr += 1
    day_diff = (curr_date-start_date).days+start_date_mahina_idx+num_sd_bef_curr - num_sd_bef_start
    mahina_day_idx = day_diff % 30
    return mahina_day_idx

####################################################################


# provided: determine if a string is a date, and parse the date
def is_date(msg):
    try:
        date = parser.parse(msg)
        return True 
    except ValueError:
        return False
def get_date(msg):
    date = parser.parse(msg)
    return date

# provided: read in mahina calendar info
def warm_up():
    with open('mahina_calendar_special_day.txt','r') as f:
        for line in f:
            date = get_date(line.strip())
            special_days.append(date)
    with open('mahina_calendar_day_name.txt','r') as f:
        for line in f:
            name, date = line.strip().split()
            mahina_day_names.append(name)
    
    with open('mahina_calendar_day_info.txt','r') as f:
        for line in f:
            date, *info = line.strip().split()
            info = ' '.join(info)
            mahina_day_infos.append(info)

# provided: discord bot
class CalendarBot(discord.Client):
    async def on_ready(self):
        # Runs when successfully connected to the server
        print('Logged on as', self.user)
        warm_up()

    async def on_message(self, message):
        # don't respond to ourselves
        if message.author == self.user:
            return

        # This passes the message's text and author name as 
        reply = make_reply(message.content, message.author.name)

        if reply:
            await message.channel.send(reply)

if __name__ == "__main__":
    client = CalendarBot()
    client.run(DISCORD_TOKEN)
