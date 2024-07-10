import discord
from discord.interactions import Interaction
from discord.ui import button
import json, httpx, tls_client, threading, time, random, hashlib, sys, os
from pystyle import Center, Colorate, Colors
from discord.ui.item import Item
from flask import request, Flask, jsonify
from discord.ui import Modal, InputText
from keyauth import api

class Fore:
    BLACK = "\033[30m"
    RED = "\033[31m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    BLUE = "\033[34m"
    MAGENTA = "\033[35m"
    CYAN = "\033[36m"
    WHITE = "\033[37m"
    UNDERLINE = "\033[4m"
    RESET = "\033[0m"


easyboosts =print(
        Center.XCenter(
            Colorate.Vertical(
                Colors.cyan_to_blue,
                f"""                                 
                                                 

░██╗░░░░░░░██╗██╗░░██╗██╗████████╗██╗░░░██╗░█████╗░
░██║░░██╗░░██║██║░░██║██║╚══██╔══╝██║░░░██║██╔══██╗
░╚██╗████╗██╔╝███████║██║░░░██║░░░╚██╗░██╔╝██║░░██║
░░████╔═████║░██╔══██║██║░░░██║░░░░╚████╔╝░██║░░██║
░░╚██╔╝░╚██╔╝░██║░░██║██║░░░██║░░░░░╚██╔╝░░╚█████╔╝
░░░╚═╝░░░╚═╝░░╚═╝░░╚═╝╚═╝░░░╚═╝░░░░░░╚═╝░░░░╚════╝░
                                                    Made by whitvo  
                                                        
    """,
                1,
            )
        )
    )

leonop = """➤ BUY THE BOOST BOT FROM OUR SHOP"""

print(f'{Fore.CYAN}{easyboosts}{Fore.RESET}')
print(f'{Fore.CYAN}{leonop}{Fore.RESET}')

os.system("title " + "BOOST BOT")

app = Flask(__name__)

def getchecksum():
    md5_hash = hashlib.md5()
    file = open(''.join(sys.argv), "rb")
    md5_hash.update(file.read())
    digest = md5_hash.hexdigest()
    return digest



config = json.load(open("config.json", encoding="utf-8"))

class Booster:
    def __init__(self) -> None:
        self.proxy = self.getProxy()
        self.getCookies()
        self.client = tls_client.Session(
            client_identifier="chrome_107",
            ja3_string="771,4866-4867-4865-49196-49200-49195-49199-52393-52392-49327-49325-49188-49192-49162-49172-163-159-49315-49311-162-158-49314-49310-107-106-103-64-57-56-51-50-157-156-52394-49326-49324-49187-49191-49161-49171-49313-49309-49233-49312-49308-49232-61-192-60-186-53-132-47-65-49239-49235-49238-49234-196-195-190-189-136-135-69-68-255,0-11-10-35-16-22-23-49-13-43-45-51-21,29-23-30-25-24,0-1-2",
            h2_settings={
                "HEADER_TABLE_SIZE": 65536,
                "MAX_CONCURRENT_STREAMS": 1000,
                "INITIAL_WINDOW_SIZE": 6291456,
                "MAX_HEADER_LIST_SIZE": 262144,
            },
            h2_settings_order=[
                "HEADER_TABLE_SIZE",
                "MAX_CONCURRENT_STREAMS",
                "INITIAL_WINDOW_SIZE",
                "MAX_HEADER_LIST_SIZE",
            ],
            supported_signature_algorithms=[
                "ECDSAWithP256AndSHA256",
                "PSSWithSHA256",
                "PKCS1WithSHA256",
                "ECDSAWithP384AndSHA384",
                "PSSWithSHA384",
                "PKCS1WithSHA384",
                "PSSWithSHA512",
                "PKCS1WithSHA512",
            ],
            supported_versions=["GREASE", "1.3", "1.2"],
            key_share_curves=["GREASE", "X25519"],
            cert_compression_algo="brotli",
            pseudo_header_order=[":method", ":authority", ":scheme", ":path"],
            connection_flow=15663105,
            header_order=["accept", "user-agent", "accept-encoding", "accept-language"],
        )
        self.failed = []
        self.success = []
        self.captcha = []
        if config["proxyless"] == False:
            self.client.proxies = self.proxy

    def getProxy(self):
        try:
            proxy = random.choice(open("data/proxies.txt", "r").read().splitlines())
            return {"http": f"http://{proxy}", "https": f"http://{proxy}"}
        except Exception as e:
            pass

    def getCookies(self, session=None):
        headers = {
            "accept": "*/*",
            "accept-language": "en-US,en;q=0.5",
            "connection": "keep-alive",
            "host": "canary.discord.com",
            "referer": "https://canary.discord.com/",
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-origin",
            "user-agent": "Mozilla/5.0 (Macintosh; U; PPC Mac OS X; de-de) AppleWebKit/85.8.5 (KHTML, like Gecko) Safari/85",
            "x-context-properties": "eyJsb2NhdGlvbiI6IkFjY2VwdCBJbnZpdGUgUGFnZSJ9",
            "x-debug-options": "bugReporterEnabled",
            "x-discord-locale": "en-US",
            "x-super-properties": "eyJvcyI6Ik1hYyBPUyBYIiwiYnJvd3NlciI6IlNhZmFyaSIsImRldmljZSI6IiIsInN5c3RlbV9sb2NhbGUiOiJlbi1KTSIsImJyb3dzZXJfdXNlcl9hZ2VudCI6Ik1vemlsbGEvNS4wIChNYWNpbnRvc2g7IFU7IFBQQyBNYWMgT1MgWDsgZGUtZGUpIEFwcGxlV2ViS2l0Lzg1LjguNSAoS0hUTUwsIGxpa2UgR2Vja28pIFNhZmFyaS84NSIsImJyb3dzZXJfdmVyc2lvbiI6IiIsIm9zX3ZlcnNpb24iOiIiLCJyZWZlcnJlciI6IiIsInJlZmVycmluZ19kb21haW4iOiIiLCJyZWZlcnJlcl9jdXJyZW50IjoiIiwicmVmZXJyaW5nX2RvbWFpbl9jdXJyZW50IjoiIiwicmVsZWFzZV9jaGFubmVsIjoic3RhYmxlIiwiY2xpZW50X2J1aWxkX251bWJlciI6MTgxODMyLCJjbGllbnRfZXZlbnRfc291cmNlIjoibnVsbCJ9",
        }
        response = httpx.get(
            "https://canary.discord.com/api/v9/experiments", headers=headers
        )
        self.dcfduid = response.cookies.get("__dcfduid")
        self.sdcfduid = response.cookies.get("__sdcfduid")
        self.cfruid = response.cookies.get("__cfruid")

    def boost(self, token, invite, guild):
        headers = {
            "authority": "discord.com",
            "accept": "*/*",
            "accept-language": "fr-FR,fr;q=0.9",
            "authorization": token,
            "cache-control": "no-cache",
            "content-type": "application/json",
            "cookie": f"__dcfduid={self.dcfduid}; __sdcfduid={self.sdcfduid}; __cfruid={self.cfruid}; locale=en-US",
            "origin": "https://discord.com",
            "pragma": "no-cache",
            "referer": "https://discord.com/channels/@me",
            "sec-ch-ua": '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": '"Windows"',
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-origin",
            "user-agent": "Mozilla/5.0 (Macintosh; U; PPC Mac OS X; de-de) AppleWebKit/85.8.5 (KHTML, like Gecko) Safari/85",
            "x-debug-options": "bugReporterEnabled",
            "x-discord-locale": "en-US",
            "x-super-properties": "eyJvcyI6Ik1hYyBPUyBYIiwiYnJvd3NlciI6IlNhZmFyaSIsImRldmljZSI6IiIsInN5c3RlbV9sb2NhbGUiOiJlbi1KTSIsImJyb3dzZXJfdXNlcl9hZ2VudCI6Ik1vemlsbGEvNS4wIChNYWNpbnRvc2g7IFU7IFBQQyBNYWMgT1MgWDsgZGUtZGUpIEFwcGxlV2ViS2l0Lzg1LjguNSAoS0hUTUwsIGxpa2UgR2Vja28pIFNhZmFyaS84NSIsImJyb3dzZXJfdmVyc2lvbiI6IiIsIm9zX3ZlcnNpb24iOiIiLCJyZWZlcnJlciI6IiIsInJlZmVycmluZ19kb21haW4iOiIiLCJyZWZlcnJlcl9jdXJyZW50IjoiIiwicmVmZXJyaW5nX2RvbWFpbl9jdXJyZW50IjoiIiwicmVsZWFzZV9jaGFubmVsIjoic3RhYmxlIiwiY2xpZW50X2J1aWxkX251bWJlciI6MTgxODMyLCJjbGllbnRfZXZlbnRfc291cmNlIjoibnVsbCJ9",
        }

        slots = httpx.get(
            "https://discord.com/api/v9/users/@me/guilds/premium/subscription-slots",
            headers=headers,
        )

        slot_json = slots.json()

        if slots.status_code == 401:
            self.failed.append(token)
            return

        if slots.status_code != 200 or len(slot_json) == 0:
            return

        r = self.client.post(
            f"https://discord.com/api/v9/invites/{invite}", headers=headers, json={}
        )

        if r.status_code == 200:
            boostsList = []
            for boost in slot_json:
                boostsList.append(boost["id"])

            payload = {"user_premium_guild_subscription_slot_ids": boostsList}

            headers["method"] = "PUT"
            headers["path"] = f"/api/v9/guilds/{guild}/premium/subscriptions"

            boosted = self.client.put(
                f"https://discord.com/api/v9/guilds/{guild}/premium/subscriptions",
                json=payload,
                headers=headers,
            )

            if boosted.status_code == 201:
                self.success.append(token)
                return True
            else:
                self.failed.append(token)

        elif r.status_code == 400:
            self.failed.append(token)

        elif r.status_code != 200:
            print(r.json())

    def nick(self, token, guild, nick):
        headers = {
            "authority": "discord.com",
            "accept": "*/*",
            "accept-language": "fr-FR,fr;q=0.9",
            "authorization": token,
            "cache-control": "no-cache",
            "content-type": "application/json",
            "cookie": f"__dcfduid={self.dcfduid}; __sdcfduid={self.sdcfduid}; __cfruid={self.cfruid}; locale=en-US",
            "origin": "https://discord.com",
            "pragma": "no-cache",
            "referer": "https://discord.com/channels/@me",
            "sec-ch-ua": '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": '"Windows"',
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-origin",
            "user-agent": "Mozilla/5.0 (Macintosh; U; PPC Mac OS X; de-de) AppleWebKit/85.8.5 (KHTML, like Gecko) Safari/85",
            "x-debug-options": "bugReporterEnabled",
            "x-discord-locale": "en-US",
            "x-super-properties": "eyJvcyI6Ik1hYyBPUyBYIiwiYnJvd3NlciI6IlNhZmFyaSIsImRldmljZSI6IiIsInN5c3RlbV9sb2NhbGUiOiJlbi1KTSIsImJyb3dzZXJfdXNlcl9hZ2VudCI6Ik1vemlsbGEvNS4wIChNYWNpbnRvc2g7IFU7IFBQQyBNYWMgT1MgWDsgZGUtZGUpIEFwcGxlV2ViS2l0Lzg1LjguNSAoS0hUTUwsIGxpa2UgR2Vja28pIFNhZmFyaS84NSIsImJyb3dzZXJfdmVyc2lvbiI6IiIsIm9zX3ZlcnNpb24iOiIiLCJyZWZlcnJlciI6IiIsInJlZmVycmluZ19kb21haW4iOiIiLCJyZWZlcnJlcl9jdXJyZW50IjoiIiwicmVmZXJyaW5nX2RvbWFpbl9jdXJyZW50IjoiIiwicmVsZWFzZV9jaGFubmVsIjoic3RhYmxlIiwiY2xpZW50X2J1aWxkX251bWJlciI6MTgxODMyLCJjbGllbnRfZXZlbnRfc291cmNlIjoibnVsbCJ9",
        }

        payload = {"nick": nick}

        httpx.patch(
            f"https://discord.com/api/v9/guilds/{guild}/members/@me",
            headers=headers,
            json=payload,
        )

        httpx.patch(
            f"https://discord.com/api/v9/users/@me/profile",
            headers=headers,
            json={"bio": nick},
        )

    def nickThread(self, tokens, guild, nick):
        """"""
        threads = []

        for i in range(len(tokens)):
            token = tokens[i]
            t = threading.Thread(target=self.nick, args=(token, guild, nick))
            t.daemon = True
            threads.append(t)

        for i in range(len(tokens)):
            threads[i].start()

        for i in range(len(tokens)):
            threads[i].join()

        return True

    def thread(self, invite, tokens, guild):
        """"""
        threads = []

        for i in range(len(tokens)):
            token = tokens[i]
            t = threading.Thread(target=self.boost, args=(token, invite, guild))
            t.daemon = True
            threads.append(t)

        for i in range(len(tokens)):
            threads[i].start()

        for i in range(len(tokens)):
            threads[i].join()

        return {
            "success": self.success,
            "failed": self.failed,
            "captcha": self.captcha,
        }



bot = discord.Bot(intents=discord.Intents.all())


def getStock(filename: str):
    tokens = []
    for i in open(filename, "r").read().splitlines():
        if ":" in i:
            i = i.split(":")[2]
            tokens.append(i)
        else:
            tokens.append(i)
    return tokens


def getinviteCode(inv):
    if "discord.gg" not in inv:
        return inv
    if "discord.gg" in inv:
        invite = inv.split("discord.gg/")[1]
        return invite
    if "https://discord.gg" in inv:
        invite = inv.split("https://discord.gg/")[1]
        return invite


def checkInvite(invite: str):
    data = httpx.get(
        f"https://discord.com/api/v9/invites/{invite}?inputValue={invite}&with_counts=true&with_expiration=true"
    ).json()

    if data["code"] == 10006:
        return False
    elif data:
        return data["guild"]["id"]
    else:
        return False


class BoostModal(Modal):
    def __init__(self):
        super().__init__(title = "Boost")
        self.add_item(
            InputText(
                label = "Invite",
                placeholder = "Invite code of the server.",
                required = True,
                style = discord.InputTextStyle.short
            )
        )

        self.add_item(
            InputText(
                label = "Amount",
                placeholder = "Amount of boosts (must be in numbers).",
                required = True,
                style = discord.InputTextStyle.short
            )
        )

        self.add_item(
            InputText(
                label = "Months",
                placeholder = "Number of months (1/3).",
                required = True,
                style = discord.InputTextStyle.short
            )
        )

        self.add_item(
            InputText(
                label = "Nick",
                placeholder = "Nickname and bio.",
                required = True,
                style = discord.InputTextStyle.short
            )
        )

    async def callback(self, ctx: discord.Interaction):

        invite = self.children[0].value

        amount = int(self.children[1].value)

        months = int(self.children[2].value)

        nick = self.children[3].value

        await ctx.response.defer()

        if amount % 2 != 0:
            return await ctx.followup.send(
                embed=discord.Embed(
                    title="**ERROR**",
                    description="❎ | Number of boosts should be in numbers.",
                    color=0xC80000,
                )
            )

        if months != 1 and months != 3:
            return await ctx.followup.send(
                embed=discord.Embed(
                    title="**ERROR**",
                    description="❎ | Invalid months [VALID INPUTS: 1/3].",
                    color=0xC80000,
                )
            )

        inviteCode = getinviteCode(invite)
        inviteData = checkInvite(inviteCode)

        if inviteData == False:
            return await ctx.followup.send(
                embed=discord.Embed(
                    title="**ERROR**",
                    description="❎ | Invalid invite provided.",
                    color=0xC80000,
                )
            )

        if months == 1:
            filename = "data/1m.txt"
        if months == 3:
            filename = "data/3m.txt"

        tokensStock = getStock(filename)
        requiredStock = int(amount / 2)

        if requiredStock > len(tokensStock):
            return await ctx.followup.send(
                embed=discord.Embed(
                    title="**ERROR**",
                    description=f"❎ | We don't have enough tokens in stock\nUse `/restock` command to restock.",
                    color=0xC80000,
                )
            )

        boost = Booster()

        tokens = []

        for x in range(requiredStock):
            tokens.append(tokensStock[x])
            remove(tokensStock[x], filename)

        await ctx.followup.send(
            embed=discord.Embed(
                title="Boost Bot", description=f"Boosting....", color=0x5598D2
            )
        )

        start = time.time()
        status = boost.thread(inviteCode, tokens, inviteData)

        time_taken = round(time.time() - start, 2)

        await ctx.followup.send(
            embed=discord.Embed(
                title="**Boosts Successful**",
                description=f"**__Amount__ ->**  {amount} boosts \n**__Months__ ->** {months}m \n**__Server Link__ ->** .gg/{inviteCode} \n**__Tokens used__ ->** {requiredStock} \n**__Successfull tokens__ ->** {len(status['success'])} \n**__Failed tokens__ ->** {len(status['failed'])}\n**__Captcha tokens__ ->** {len(status['captcha'])} \n**__Time taken__ ->** {time_taken}s",
                color=0x5598D2,
            )
        )

        boost.nickThread(tokens, inviteData, nick)


@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.dnd, activity=discord.Activity(type=discord.ActivityType.listening, name='Best Boost Bot'))
    print(f"{Fore.BLUE} [BOT]: {bot.user} is online.{Fore.RESET}")


@bot.slash_command(
    guild_ids=config["dev-guilds"], name="boost", description="Boost a server by using that command."
)
async def boost(
    ctx: discord.Interaction
    # invite: discord.Option(str, "Invite code of the server.", required=True),
    # amount: discord.Option(
    #     int, "Amount of boosts (must be in numbers).", required=True
    # ),
    # months: discord.Option(int, "Number of months (1/3).", required=True),
    # nick: discord.Option(str, "Nickname and bio.", required=True),
):

    if str(ctx.author.id) not in config["owners"]:
        return await ctx.respond(
            embed=discord.Embed(
                title="**ERROR**",
                description="❎ | Missing permissions, you cannot use this command.",
                color=0xC80000,
            )
        )

    modal = BoostModal()
    await ctx.response.send_modal(modal)


    # if amount % 2 != 0:
    #     return await ctx.respond(
    #         embed=discord.Embed(
    #             title="**ERROR**",
    #             description="Number of boosts should be in numbers.",
    #             color=0xC80000,
    #         )
    #     )

    # if months != 1 and months != 3:
    #     return await ctx.respond(
    #         embed=discord.Embed(
    #             title="**ERROR**",
    #             description="Invalid months [VALID INPUTS: 1/3].",
    #             color=0xC80000,
    #         )
    #     )

    # inviteCode = getinviteCode(invite)
    # inviteData = checkInvite(inviteCode)

    # if inviteData == False:
    #     return await ctx.respond(
    #         embed=discord.Embed(
    #             title="**ERROR**",
    #             description="Invalid invite provided.",
    #             color=0xC80000,
    #         )
    #     )

    # if months == 1:
    #     filename = "data/1m.txt"
    # if months == 3:
    #     filename = "data/3m.txt"

    # tokensStock = getStock(filename)
    # requiredStock = int(amount / 2)

    # if requiredStock > len(tokensStock):
    #     return await ctx.respond(
    #         embed=discord.Embed(
    #             title="**ERROR**",
    #             description=f"We don't have enough tokens in stock\nUse `/restock` command to restock.",
    #             color=0xC80000,
    #         )
    #     )

    # boost = Booster()

    # tokens = []

    # for x in range(requiredStock):
    #     tokens.append(tokensStock[x])
    #     remove(tokensStock[x], filename)

    # await ctx.respond(
    #     embed=discord.Embed(
    #         title="Boost Bot", description=f"Boosting....", color=0x5598D2
    #     )
    # )

    # start = time.time()
    # status = boost.thread(inviteCode, tokens, inviteData)

    # time_taken = round(time.time() - start, 2)

    # await ctx.edit(
    #     embed=discord.Embed(
    #         title="**Boosts Successful**",
    #         description=f"**__Amount__ ->**  {amount} boosts \n**__Months__ ->** {months}m \n**__Server Link__ ->** .gg/{inviteCode} \n**__Tokens used__ ->** {requiredStock} \n**__Successfull tokens__ ->** {len(status['success'])} \n**__Failed tokens__ ->** {len(status['failed'])}\n**__Captcha tokens__ ->** {len(status['captcha'])} \n**__Time taken__ ->** {time_taken}s",
    #         color=0x5598D2,
    #     )
    # )

    # boost.nickThread(tokens, inviteData, nick)

    # return True


@bot.slash_command(
    guild_ids=config["dev-guilds"], name="addadmin", description="Add an admin to use the bot command."
)
async def addadmin(
    ctx,
    member: discord.Option(discord.Member, "The member you want to add.", required=True),
):
    await ctx.defer(ephemeral=False)
    if str(ctx.author.id) not in config["owners"]:
        return await ctx.respond(
            embed=discord.Embed(
                title="**ERROR**",
                description="❎ | You cannot use this command.",
                color=0xC80000,
            )
        )

    config["admins"].append(str(member.id))
    with open("config.json", "w") as f:
        json.dump(config, f, indent=4)

    return await ctx.edit(
        embed=discord.Embed(
            title="Boost Bot",
            description=f"✅ | Added the member to admin successfully.",
            color=0x5598D2,
        )
    )


def remove(token: str, filename: str):
    tokens = getStock(filename)
    tokens.pop(tokens.index(token))
    f = open(filename, "w")

    for x in tokens:
        f.write(f"{x}\n")

    f.close()


class PanelView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)


    @button(emoji = "🚀", custom_id="panelboost")
    async def panel_boost(self, button, interaction):
        await interaction.response.send_modal(BoostModal())

    @button(emoji = "📂", custom_id="panelstock")
    async def panel_stock(self, button, interaction):
        await interaction.response.send_modal(StockModal())

    @button(emoji = "📜", custom_id="panelrestock")
    async def panel_restock(self, button, interaction):
        await interaction.response.send_modal(RestockModal())

    @button(emoji = "💸", custom_id="panelgivetoken")
    async def panel_givetoken(self, button, interaction):
        await interaction.response.send_modal(SendtokensModal())


@bot.slash_command(
   guild_ids=config["dev-guilds"], name="panel", description="Shows the boost bot panel."
)
async def panel(
    ctx
):
    embed = discord.Embed(
        title = "القائمه الرئيسيه"
    ).add_field(
        name = "الخيارات المتاحه : ",
        value = "🚀 بوست للسيرفر\n📂 مشاهده الكميه\n📜 تخزين توكن\n💸 اهداء توكن من المخزن"
    ).set_thumbnail(url = "https://cdn.discordapp.com/attachments/1126283697512001657/1197847477936722040/wwwq.png?ex=65bcc165&is=65aa4c65&hm=e5983c42a33469ff16d340ce9ed94be9c336b550fb3c57f84847a54fa866b735&")

    await ctx.respond(embed = embed, view = PanelView())

class SendtokensModal(Modal):
    def __init__(self):
        super().__init__(title = "Send Tokens")

        self.add_item(
            InputText(
                label = "   الشخص ID   ",
                placeholder = " حط الكوبي ايدي للشخص الي تبي ترسله التوكنات ",
                required = True,
                style = discord.InputTextStyle.short
            )
        )

        self.add_item(
            InputText(
                label = "عدد التوكنات ",
                placeholder = " حط عدد التوكنات الي تبي تعطي الشخص ",
                required = True,
                style = discord.InputTextStyle.short
            )
        )

        self.add_item(
            InputText(
                label = "عدد الاشهر ",
                placeholder = " حط النوع التوكن الي تبي تعطيه اياه شهر او 3 اشهر",
                required = True,
                style = discord.InputTextStyle.short
            )
        )


    async def callback(self, ctx):



        member = ctx.guild.get_member(int(self.children[0].value))
        amount = int(self.children[1].value)
        months = int(self.children[2].value)


        await ctx.response.defer()

        if months != 1 and months != 3:
            return await ctx.followup.send(
                embed=discord.Embed(
                    title="**خطأ**",
                    description="❎ | طلعت مستخدمه يبو [VALID INPUTS: 1/3].",
                    color=0xC80000,
                )
            )

        if months == 1:
            filename = "data/1m.txt"
        if months == 3:
            filename = "data/3m.txt"

        tokensStock = getStock(filename)

        if amount > len(tokensStock):
            return await ctx.followup.send(
                embed=discord.Embed(
                    title="**خطأ***",
                    description=f"❎ | عشان تشوف المخزون ( /restock )  المخزون عندك فاضي استخدم امر  ",
                    color=0xC80000,
                )
            )

        tokens = []
        for x in range(amount):
            tokens.append(tokensStock[x])
            remove(tokensStock[x], filename)

        stuff = "\n".join(tokens)

        with open("result.txt", "w") as file:
            file.write(stuff.format("\n", "\n"))

        with open("result.txt", mode="rb") as f:
            await member.send(
                embed=discord.Embed(
                    title="Boost Bot",
                    description=f"✅ | شكرا لاستخدام خدماتنا.",
                    color=0x5598D2,
                ),
                file=discord.File(f),
            )

        return await ctx.followup.send(
            embed=discord.Embed(
                title="Boost Bot",
                description=f"✅ | Sent {amount}x tokens.",
                color=0x5598D2,
            )
        )

@bot.slash_command(
    guild_ids=config["dev-guilds"], name="sendtokens", description="Sends the tokens to the user."
)
async def sendtokens(
    ctx,
    # member: discord.Option(discord.Member, "The member you want to send.", required=True),
    # amount: discord.Option(int, "Amount of tokens to send.", required=True),
    # months: discord.Option(int, "Number of months (1/3).", required=True),
):

    # if str(ctx.author.id) not in config["owners"]:
    #     return await ctx.respond(
    #         embed=discord.Embed(
    #             title="**ERROR**",
    #             description="Missing permissions, you cannot use this command.",
    #             color=0xC80000,
    #         )
    #     )

    await ctx.response.send_modal(SendtokensModal())

    # if months != 1 and months != 3:
    #     return await ctx.respond(
    #         embed=discord.Embed(
    #             title="**ERROR**",
    #             description="Invalid months [VALID INPUTS: 1/3].",
    #             color=0xC80000,
    #         )
    #     )

    # if months == 1:
    #     filename = "data/1m.txt"
    # if months == 3:
    #     filename = "data/3m.txt"

    # tokensStock = getStock(filename)

    # if amount > len(tokensStock):
    #     return await ctx.respond(
    #         embed=discord.Embed(
    #             title="**ERROR**",
    #             description=f"We don't have enough tokens in stock\nUse `/restock` command to restock.",
    #             color=0xC80000,
    #         )
    #     )

    # tokens = []
    # for x in range(amount):
    #     tokens.append(tokensStock[x])
    #     remove(tokensStock[x], filename)

    # stuff = "\n".join(tokens)

    # with open("result.txt", "w") as file:
    #     file.write(stuff.format("\n", "\n"))

    # with open("result.txt", mode="rb") as f:
    #     await member.send(
    #         embed=discord.Embed(
    #             title="Boost Bot",
    #             description=f"Thanks for using our services.",
    #             color=0x5598D2,
    #         ),
    #         file=discord.File(f),
    #     )

    # return await ctx.edit(
    #     embed=discord.Embed(
    #         title="Boost Bot",
    #         description=f"Sent {amount}x tokens.",
    #         color=0x5598D2,
    #     )
    # )


@bot.slash_command(
    guild_ids=config["dev-guilds"], name="website", description="It will send a website link."
)
async def website(
    ctx,
):
    return await ctx.respond(
        embed=discord.Embed(
            title="Website",
            description=f"Website: {config['website']}",
            color=0x5598D2,
        )
    )


@bot.slash_command(guild_ids=config["dev-guilds"], name="pp", description="It will send the paypal.")
async def pp(
    ctx,
):
    return await ctx.respond(
        embed=discord.Embed(
            title="واكتب هاذي الرسالة في الدفع",
            description=f"This is a payment for a virtual (intangible) item. Physical shipment is not required. I understand that this is a non-refundable transaction. By sending this payment, I agree that I have already received the item and I am pleased with my purchase and the item is as described. I will not chargeback as the transaction is complete. I confirm that I am the owner of this account and I authorize this payment as I continue to proceed with the payment. If I chargeback, it would be considered to be fraud/scam: {config['pp']}",
            color=0x5598D2,
        )
    )

@bot.slash_command(guild_ids=config["dev-guilds"], name="visa", description="رابط موقع الي يبي يشتري من فيزا")
async def pp(
    ctx,
):
    return await ctx.respond(
        embed=discord.Embed(
            title="💳  رابط فيزا",
            description=f" {config['visa']}",
            color=0x5598D2,
        )
    )


@bot.slash_command(guild_ids=config["dev-guilds"], name="ltc", description="It will send the litecoin address.")
async def ltc(
    ctx,
):
    return await ctx.respond(
        embed=discord.Embed(
            title="Litecoin",
            description=f"Litecoin: {config['ltc']}",
            color=0x5598D2,
        )
    )


@bot.slash_command(guild_ids=config["dev-guilds"], name="btc", description="It will send the bitcoin address.")
async def btc(
    ctx,
):
    return await ctx.respond(
        embed=discord.Embed(
            title="Bitcoin",
            description=f"Bitcoin: {config['bitcoin']}",
            color=0x5598D2,
        )
    )

class MyView(discord.ui.View):
    @discord.ui.button(label="", row=1, style=discord.ButtonStyle.grey, emoji='💰')
    async def first_button_callback(self, button, interaction):
        await interaction.response.send_message(embed=discord.Embed(
            title="__Boost Commands__",
            description="**/boost | /restock | /stock | /sendtokens**",
            color=0x5598D2,
        ))
    @discord.ui.button(label="", row=1, style=discord.ButtonStyle.grey, emoji="🍸")
    async def second_button_callback(self, button, interaction):
        await interaction.response.send_message(embed=discord.Embed(
            title='__Others Commands__',
            description='**/pp | /btc | /ltc | /ca | /website | /visa**',
            color=0x5598D2,
        ))
    @discord.ui.button(label="", row=1, style=discord.ButtonStyle.grey, emoji="🌟")
    async def third_button_callback(self, button, interaction):
        await interaction.response.send_message(embed=discord.Embed(
            title='__Owner Commands__',
            description='**/addadmin | /addowner**',
            color=0x5598D2,
        ))

@bot.slash_command(guild_ids=config["dev-guilds"], name="help", description="It will show the help menu.")
async def help(ctx):
    await ctx.respond(
        embed=discord.Embed(
            title="Help Menu",
            description="**It will show the bot all commands!**",
            color=0x5598D2
            ),
            view=MyView()
    )


@bot.slash_command(guild_ids=config["dev-guilds"], name="ca", description="It will send the cashapp.")
async def ca(
    ctx,
):
    return await ctx.respond(
        embed=discord.Embed(
            title="Cashapp",
            description=f"CashApp: {config['cashapp']}",
            color=0x5598D2,
        )
    )


@bot.slash_command(
    guild_ids=config["dev-guilds"], name="addowner", description="Add a member as a owner."
)
async def addowner(
    ctx,
    member: discord.Option(discord.Member, "The member you want to add.", required=True),
):
    await ctx.defer(ephemeral=False)
    if str(ctx.author.id) not in config["owners"]:
        return await ctx.respond(
            embed=discord.Embed(
                title="**ERROR**",
                description="❎ | You cannot use this command.",
                color=0xC80000,
            )
        )

    config["owners"].append(str(member.id))
    with open("config.json", "w") as f:
        json.dump(config, f, indent=4)

    return await ctx.edit(
        embed=discord.Embed(
            title="Boost Bot",
            description=f"✅ | Added owner successfully",
            color=0x5598D2,
        )
    )


class StockModal(Modal):
    def __init__(self):
        super().__init__(title = "Stocks")

        self.add_item(
            InputText(
                label = "Duration",
                placeholder = "Months? [1/3]",
                required = True,
                style = discord.InputTextStyle.short
            )
        )

    async def callback(self, ctx: Interaction):

        duration = int(self.children[0].value)

        await ctx.response.defer(ephemeral=False)

        if duration != 1 and duration != 3 and duration != 0:
            return await ctx.followup.send(
                embed=discord.Embed(
                    title="**ERROR**",
                    description="❎ | Invalid type. [1/3] are valid inputs.",
                    color=0xC80000,
                )
            )

        if duration == 1:
            fileName = "data/1m.txt"
        elif duration == 3:
            fileName = "data/3m.txt"

        stock = len(open(fileName, "r").readlines())

        return await ctx.followup.send(
            embed=discord.Embed(
                title=f"**__{duration} months tokens__**",
                description=f"\n -> ``We have`` **{stock}** ``tokens and`` **{stock * 2}** ``boosts in stock``",
                color=0x5598D2,
            )
        )



@bot.slash_command(
    guild_ids=config["dev-guilds"], name="stock", description="Display the stock of boosts and tokens."
)
async def stock(
    ctx
):

    await ctx.response.send_modal(StockModal())

    # await ctx.defer(ephemeral=False)


    # if duration != 1 and duration != 3 and duration != 0:
    #     return await ctx.respond(
    #         embed=discord.Embed(
    #             title="**ERROR**",
    #             description="Invalid type. [1/3] are valid inputs.",
    #             color=0xC80000,
    #         )
    #     )

    # if duration == 1:
    #     fileName = "data/1m.txt"
    # elif duration == 3:
    #     fileName = "data/3m.txt"

    # stock = len(open(fileName, "r").readlines())

    # return await ctx.edit(
    #     embed=discord.Embed(
    #         title=f"**__{type} months tokens__**",
    #         description=f"\n -> ``We have`` **{stock}** ``tokens and`` **{stock * 2}** ``boosts in stock``",
    #         color=0x5598D2,
    #     )
    # )

class RestockModal(Modal):
    def __init__(self):
        super().__init__(title = "Restock Tokens")

        self.add_item(
            InputText(
                label = "Duration",
                placeholder = "Months? [1/3]",
                required = True,
                style = discord.InputTextStyle.short
            )
        )

        self.add_item(
            InputText(
                label = "Tokens",
                placeholder = "Enter Tokens",
                required = True,
                style = discord.InputTextStyle.paragraph,
                max_length=4000
            )
        )

    async def callback(self, ctx: Interaction):
        await ctx.response.defer()

        if (
        str(ctx.user.id) not in config["owners"]
        and str(ctx.user.id) not in config["admins"]
        ):
            return await ctx.followup.send(
                embed=discord.Embed(
                    title="**ERROR**",
                    description="❎ | Missing permissions, you cannot use this command.",
                    color=0xC80000,
                )
            )

        duration = int(self.children[0].value)
        tokens = self.children[1].value.split("\n")

        if duration != 1 and duration != 3 and duration != 0:
            return await ctx.respond(
                embed=discord.Embed(
                    title="**ERROR**",
                    description="❎ | Invalid duration. [1/3] are valid inputs.",
                    color=0xC80000,
                )
            )

        if duration == 1:
            fileName = "data/1m.txt"
        elif duration == 3:
            fileName = "data/3m.txt"

        with open(fileName, "a") as f:
            for t in tokens:
                f.write(t+"\n")

        await ctx.followup.send(
            embed=discord.Embed(
                title="Boost Bot",
                description=f"✅ | Restocked successfully",
                color=0x5598D2,
            )
        )


@bot.slash_command(
    guild_ids=config["dev-guilds"], name="restock", description="Add the tokens in the stock."
)
async def restock(
    ctx,
    type: discord.Option(int, "Number of months (1/3).", required=True),
    file: discord.Option(discord.Attachment, "Attachment", required=True),
):
    await ctx.defer(ephemeral=False)

    if (
        str(ctx.author.id) not in config["owners"]
        and str(ctx.author.id) not in config["admins"]
    ):
        return await ctx.respond(
            embed=discord.Embed(
                title="**ERROR**",
                description="❎ | Missing permissions, you cannot use this command.",
                color=0xC80000,
            )
        )

    if type != 1 and type != 3 and type != 0:
        return await ctx.respond(
            embed=discord.Embed(
                title="**ERROR**",
                description="❎ | Invalid type. [1/3] are valid inputs.",
                color=0xC80000,
            )
        )

    if type == 1:
        fileName = "data/1m.txt"
    elif type == 3:
        fileName = "data/3m.txt"

    content = await file.read()

    stuff = content.decode().split("\r\n")
    before = getStock(fileName)

    for x in range(len(before)):
        stuff.append(before[x])

    cute = "\n".join(stuff)
    text = cute.replace("b'", "").replace("'", "")

    with open(fileName, "w") as file:
        file.write(text + "\n")

    return await ctx.edit(
        embed=discord.Embed(
            title="Boost Bot",
            description=f"✅ | Restocked successfully",
            color=0x5598D2,
        )
    )


orders_sellapp = []
orders_sellix = []


@app.route("/sellix", methods=["POST"])
def sellix():
    data = request.json
    if data in orders_sellix:
        pass
    elif data not in orders_sellix:
        threading.Thread(
            target=sellixshit,
            args=[
                data,
            ],
        ).start()
        orders_sellix.append(data)
    return jsonify({"message": f"We've recieved your order"}), 200


def sellixshit(data):
    """"""
    invite = ""
    title = data["data"]["product_title"].lower()

    split_parts = title.split(" | ")

    amount = int(split_parts[0].split()[0])
    months = int(split_parts[1].split()[0])

    if amount == None or months == None:
        return

    for i in data["data"]["custom_fields"]:
        if i == config["sellix"]["invite_field_name"]:
            invite = data["data"]["custom_fields"][i]

    order_id = data["data"]["uniqid"]
    email = data["data"]["customer_email"]
    product = data["data"]["product_title"]

    inviteCode = getinviteCode(invite)
    inviteData = checkInvite(inviteCode)

    embeds_data = {
        "embeds": [
            {
                "title": "**Sellix Order**",
                "description": f"**Order ID: **{order_id}\n**Email: **{email}\n**Product: **{product}\n**Amount: **{amount} Boosts\n**Months: **{months} Months\n**Invite: **[{inviteCode}](https://discord.gg/{inviteCode})",
            }
        ]
    }

    response = httpx.post(
        config["sellix"]["orders"],
        data=json.dumps(embeds_data),
        headers={"Content-Type": "application/json"},
    )

    if response.status_code == 204:
        """"""
    else:
        print(response.json())

    if inviteData == False:
        return print(f"[ERROR]: Invalid invite was provided for order: {order_id}")

    if months == 1:
        filename = "data/1m.txt"
    if months == 3:
        filename = "data/3m.txt"

    tokensStock = getStock(filename)
    requiredStock = int(amount / 2)

    if requiredStock > len(tokensStock):
        return print(
            f"[ERROR]: We didn't had enough boosts to satisfy order: {order_id}"
        )

    tokens = []

    for x in range(requiredStock):
        tokens.append(tokensStock[x])
        remove(tokensStock[x], filename)

    cool = Booster()
    status = cool.thread(inviteCode, tokens, inviteData)
    success = status["success"]
    failed = status["failed"]

    print(
        f"{Fore.GREEN}[+]: Attempted to do {Fore.BLUE}{amount}x{Fore.RESET} {Fore.GREEN}boosts for {order_id} order id. {Fore.RESET} {Fore.CYAN}\n[-]: Successfully did {Fore.RESET}{len(success)}x boost. {Fore.CYAN}\n[-]: Failed to do {Fore.RESET}{len(failed)}x boosts.\n\n    Results \n[Success]: {success}\n[Failed]: {failed} \n\n"
    )

    completed_data = {
        "embeds": [
            {
                "title": "**Sellix Completion**",
                "description": f"**Order ID: **{order_id}\n**Email: **{email}\n**Product: **{product}\n**Amount: **{amount} Boosts\n**Months: **{months} Months\n**Invite: **[{inviteCode}](https://discord.gg/{inviteCode}) \n\n**[SUCCESS]**: {success} \n**[FAILED]**: {failed}",
            }
        ]
    }

    response = httpx.post(
        config["sellapp"]["orders"],
        data=json.dumps(completed_data),
        headers={"Content-Type": "application/json"},
    )

    if response.status_code == 204:
        """"""
    else:
        print(response.json())


@app.route("/sellapp", methods=["POST"])
def sellapp():
    data = request.json
    order_id = data["invoice"]["id"]

    if order_id in orders_sellapp:
        pass
    elif order_id not in orders_sellapp:
        threading.Thread(
            target=sellshit,
            args=[
                data,
            ],
        ).start()
        orders_sellapp.append(order_id)
    return jsonify({"message": f"We've recieved your order"}), 200


def sellshit(data):
    """"""
    invite = ""

    for i in data["additional_information"]:
        if i["label"] == config["sellapp"]["invite_field_name"]:
            invite = i["value"]

    title = data["listing"]["title"]

    split_parts = title.split(" | ")

    amount = int(split_parts[0].split()[0])
    months = int(split_parts[1].split()[0])

    if amount == None or months == None:
        return

    inviteCode = getinviteCode(invite)
    inviteData = checkInvite(inviteCode)

    order_id = data["invoice"]["id"]
    email = data["invoice"]["payment"]["gateway"]["data"]["customer_email"]
    product = data["listing"]["title"]

    embeds_data = {
        "embeds": [
            {
                "title": "**SellApp Order**",
                "description": f"**Order ID: **{order_id}\n**Email: **{email}\n**Product: **{product}\n**Amount: **{amount} Boosts\n**Months: **{months} Months\n**Invite: **[{inviteCode}](https://discord.gg/{inviteCode})",
            }
        ]
    }

    response = httpx.post(
        config["sellapp"]["orders"],
        data=json.dumps(embeds_data),
        headers={"Content-Type": "application/json"},
    )

    if response.status_code == 204:
        """"""
    else:
        print(response.json())

    if inviteData == False:
        return print(f"[ERROR]: Invalid invite was provided for order: {order_id}")

    if months == 1:
        filename = "data/1m.txt"
    if months == 3:
        filename = "data/3m.txt"

    tokensStock = getStock(filename)
    requiredStock = int(amount / 2)

    if requiredStock > len(tokensStock):
        return print(
            f"[ERROR]: We didn't had enough boosts to satisfy order: {order_id}"
        )

    tokens = []

    for x in range(requiredStock):
        tokens.append(tokensStock[x])
        remove(tokensStock[x], filename)

    cool = Booster()
    status = cool.thread(inviteCode, tokens, inviteData)
    success = status["success"]
    failed = status["failed"]

    print(
        f"{Fore.GREEN}[+]: Attempted to do {Fore.BLUE}{amount}x{Fore.RESET} {Fore.GREEN}boosts for {order_id} order id. {Fore.RESET} {Fore.CYAN}\n[-]: Successfully did {Fore.RESET}{len(success)}x boost. {Fore.CYAN}\n[-]: Failed to do {Fore.RESET}{len(failed)}x boosts.\n\n    Results \n[Success]: {success}\n[Failed]: {failed} \n\n"
    )

    completed_data = {
        "embeds": [
            {
                "title": "**SellApp Completion**",
                "description": f"**Order ID: **{order_id}\n**Email: **{email}\n**Product: **{product}\n**Amount: **{amount} Boosts\n**Months: **{months} Months\n**Invite: **[{inviteCode}](https://discord.gg/{inviteCode}) \n\n**[SUCCESS]**: {success} \n**[FAILED]**: {failed}",
            }
        ]
    }

    response = httpx.post(
        config["sellapp"]["orders"],
        data=json.dumps(completed_data),
        headers={"Content-Type": "application/json"},
    )

    if response.status_code == 204:
        """"""
    else:
        print(response.json())

def serve():
    app.run(host="0.0.0.0", port=config["port"])

def startServer():
    server = threading.Thread(target=serve)
    server.start()

startServer();
bot.run(config["token"])