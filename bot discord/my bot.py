

#import



import discord 
import os 
import requests
import asyncio
import random
import json
import time
from discord.ext import commands
from discord.ui import Button, View
from discord.ext import commands, tasks
from datetime import datetime


intents = discord.Intents.all()
bot = commands.Bot(command_prefix='!', intents=intents)




owner = ['1304154596029108227']





@bot.event
async def on_ready():
    bot.launch_time = discord.utils.utcnow()  
    print(f"Bot connecté en tant que {bot.user}")



#bonjour


@bot.command()
async def bonjour(ctx, member: discord.Member):
    if commands :
        await ctx.send(f"Bonjour{member.mention}! 👋")
    







#pile ou face 


@bot.command()
async def coinflip(ctx):
    await ctx.send("🪙 **Jeu de Pile ou Face**\nChoisis entre 'pile' ou 'face' pour jouer !")

    def check(message):
        return message.author == ctx.author and message.content.lower() in ['pile', 'face']

    try:
        
        choix = await bot.wait_for('message', check=check, timeout=30.0)

        
        resultat = random.choice(['pile', 'face'])

        
        embed = discord.Embed(
            title="Résultat du Pile ou Face 🎲",
            color=discord.Color.blue()
        )
        embed.add_field(name="Choix de l'utilisateur", value=f"Tu as choisi : {choix.content.capitalize()}", inline=False)
        embed.add_field(name="Résultat", value=f"Le résultat est : **{resultat.capitalize()}**", inline=False)

        if choix.content.lower() == resultat:
            embed.add_field(name="🎉 Félicitations !", value=f"Bravo {ctx.author.mention}, tu as gagné !", inline=False)
            embed.set_thumbnail(url="https://cdn-icons-png.flaticon.com/512/535/535611.png")  
        else:
            embed.add_field(name="😢 Désolé !", value=f"Tu as perdu {ctx.author.mention}. Essaie encore !", inline=False)
            embed.set_thumbnail(url="https://cdn-icons-png.flaticon.com/512/535/535613.png")  

        
        await ctx.send(embed=embed)

    except asyncio.TimeoutError:
        await ctx.send(f"⏰ Désolé {ctx.author.mention}, tu n'as pas répondu à temps. Essaie à nouveau !")






#ping du code 

@bot.command()
async def ping(ctx):
    latency = round(bot.latency * 1000)  
    
    embed = discord.Embed(
        title="🏓 **Pong!**",
        description=f"Le **ping** du bot est de **{latency} ms**.",
        color=discord.Color.green()  
    )

    
    embed.set_thumbnail(url="https://cdn-icons-png.flaticon.com/512/137/137578.png")

    
    embed.set_footer(text="Réponse rapide pour un bot réactif !", icon_url="https://cdn-icons-png.flaticon.com/512/1234/1234356.png")

    
    await ctx.send(embed=embed)

















# clear

@bot.command()
async def clear(ctx, amount: int = 1):  
    if amount <= 0:
        await ctx.send(":x: Veuillez indiquer un nombre de messages positif.")
        return

   
    deleted = await ctx.channel.purge(limit=amount + 1)

    
    embed = discord.Embed(
        title="🧹 **Nettoyage de messages**",
        description=f"{len(deleted)} messages ont été supprimés avec succès.",
        color=discord.Color.red()  
    )
    embed.set_thumbnail(url="https://cdn-icons-png.flaticon.com/512/561/561125.png")
    embed.set_footer(text=f"Commande exécutée par {ctx.author.name}", icon_url=ctx.author.avatar.url)

   
    await ctx.send(embed=embed, delete_after=5)






#ban liste


@bot.command()
async def banworld(ctx, member: discord.User):
   
    if not ctx.author.guild_permissions.ban_members:
        return await ctx.send("❌ Vous n'avez pas la permission d'utiliser cette commande.")

    
    if not ctx.guild.me.guild_permissions.ban_members:
        return await ctx.send("❌ Je n'ai pas la permission de bannir dans ce serveur.")

    success = 0
    failure = 0

    
    for guild in bot.guilds:
        
        target_member = guild.get_member(member.id)
        if target_member:
            try:
                
                await guild.ban(target_member, reason=f"Banni globalement par {ctx.author}")
                success += 1
            except discord.Forbidden:
                failure += 1  
            except discord.HTTPException:
                failure += 1  
        else:
            failure += 1  

    
    await ctx.send(
        f"✅ {success} serveurs où {member.mention} a été banni.\n"
        f"❌ {failure} serveurs où l'utilisateur n'a pas pu être banni."
    )











#blagues




blagues = [
    "Pourquoi les plongeurs plongent-ils toujours en arrière et jamais en avant ? Parce que sinon ils tombent toujours dans le bateau !",
    "Pourquoi les poissons détestent l'ordinateur ? Parce qu’ils ont peur du net !",
    "Que dit un escargot lorsqu’il monte sur le dos d’une tortue ? Wouhou !",
    "Pourquoi les squelettes ne se battent-ils jamais entre eux ? Parce qu’ils n’ont pas le cran !",
    "Quel est le comble pour un électricien ? De ne pas être au courant !",
    "Pourquoi les vaches regardent-elles toujours les trains passer ? Parce qu’elles trouvent ça trainant !",
    "Pourquoi les plongeurs n’aiment-ils jamais les poissons rouges ? Parce qu’ils les trouvent un peu flippants !",
    "Comment appelle-t-on un chien qui fait de la magie ? Un labracadabrador !",
    "Pourquoi les livres détestent-ils l'eau ? Parce qu’ils ont peur de se noyer dans leurs propres pages !",
    "Que fait une abeille dans une église ? Elle prie !"
]

@bot.command()
async def blague(ctx):
    blague_choisie = random.choice(blagues)

    #
    embed = discord.Embed(
        title="😂 Blague du Jour",
        description=f"**{blague_choisie}**",
        color=discord.Color.orange()
    )
    embed.set_footer(text="Parce qu'une bonne blague, ça fait toujours du bien !")

    
    await ctx.send(embed=embed)






#compliments




compliments = [
    "Tu es incroyable, ne change jamais ! 🌟",
    "Tu rends le monde meilleur rien qu’en étant là ! 😊",
    "Ton sourire illumine la journée de tout le monde ! 😄",
    "Tu as un talent incroyable, ne le sous-estime pas ! 🎨",
    "Ton enthousiasme est contagieux ! 🌈",
    "Tu es une source d’inspiration pour les autres. Continue comme ça ! 💪",
    "Chaque jour à tes côtés est une bénédiction ! ✨",
    "Ton esprit est aussi beau que ton sourire ! 😍",
    "Tu es un(e) ami(e) précieux(se) et irremplaçable ! ❤️",
    "Avec toi, tout devient plus simple et plus joyeux ! 🌸",
    "Tu as une manière unique de résoudre les problèmes. C'est impressionnant ! 🧠",
    "Les gens ont de la chance de te connaître ! 🍀",
    "Ta gentillesse rend le monde meilleur. Merci d’être toi ! 💖",
    "Tu es un(e) vrai(e) champion(ne) dans ce que tu fais ! 🏆",
    "Tu es la définition du mot « génial » ! 😎"
]

@bot.command()
async def compliment(ctx, member: discord.Member = None):
    if not member:
        await ctx.send(":x: **Mentionne quelqu'un pour lui faire un compliment !**")
    else:
        compliment_message = random.choice(compliments)

        
        embed = discord.Embed(
            title="💖 Compliment du Jour",
            description=f"{member.mention}, {compliment_message}",
            color=discord.Color.yellow()
        )
        embed.set_footer(text="Parce que tout le monde mérite un compliment ! 😊")
        
        
        await ctx.send(embed=embed)







#mute

@bot.command()
async def mute(ctx, member: discord.Member = None):
    guild = ctx.guild
    role_name = "muted"

    if not member:
        await ctx.send(":x: Veuillez mentionner la personne que vous voulez mute.")
        return

    mute_role = discord.utils.get(guild.roles, name=role_name)

    
    
    if not mute_role:
        mute_role = await guild.create_role(name=role_name)

        for channel in guild.text_channels:
            await channel.set_permissions(mute_role, send_messages=False)

    
    
    if mute_role not in member.roles:
        await member.add_roles(mute_role)
        
        embed = discord.Embed(
            title="🔇 **Membre Mute**",
            description=f"{member.mention} a été **muté** et ne peut plus envoyer de messages.",
            color=discord.Color.orange()
        )
        embed.set_thumbnail(url=member.avatar.url)
        embed.add_field(name="Raison", value="Aucune raison spécifiée", inline=False)
        embed.set_footer(text=f"Commandé par {ctx.author.name}", icon_url=ctx.author.avatar.url)
        
        await ctx.send(embed=embed)
    else:
        await ctx.send(f"{member.mention} est déjà muté.")




@bot.command()
async def unmute(ctx, member: discord.Member = None):
    if not member:
        await ctx.send(":x: Veuillez mentionner le membre que vous voulez unmute.")
        return

    guild = ctx.guild
    role_name = "muted"
    mute_role = discord.utils.get(guild.roles, name=role_name)

    
    if mute_role in member.roles:
        await member.remove_roles(mute_role)
        
        embed = discord.Embed(
            title="🔊 **Membre Unmute**",
            description=f"{member.mention} peut désormais **envoyer des messages**.",
            color=discord.Color.green()
        )
        embed.set_thumbnail(url=member.avatar.url)
        embed.add_field(name="Raison", value="Aucune raison spécifiée", inline=False)
        embed.set_footer(text=f"Commandé par {ctx.author.name}", icon_url=ctx.author.avatar.url)

        await ctx.send(embed=embed)
    else:
        await ctx.send(f"{member.mention} n'est pas muté.")



   




#serveur info


@bot.command()
async def serveur_info(ctx):
    server = ctx.guild

  
    embed = discord.Embed(
        title="📊 **Informations sur le serveur**",
        description=f"Voici un aperçu détaillé de **{server.name}**",
        color=discord.Color.green()
    )
    
    
    embed.add_field(name="📅 Créé le", value=server.created_at.strftime("%d/%m/%Y à %H:%M"), inline=True)
    embed.add_field(name="👑 Propriétaire", value=server.owner.mention, inline=True)
    embed.add_field(name="🧑‍🤝‍🧑 Nombre de membres", value=server.member_count, inline=True)
    embed.add_field(name="🌐 Système de vérification", value=server.verification_level.name, inline=True)
    embed.add_field(name="🖼️ Avatar du serveur", value=f"[Voir l'avatar]({server.icon.url})", inline=False)
    
    
    highest_role = server.roles[-1] if server.roles else None
    embed.add_field(name="🏅 Rôle le plus élevé", value=highest_role.name if highest_role else "Aucun rôle", inline=True)
    
    
    embed.add_field(name="⏳ Date d'adhésion", value=server.members[0].joined_at.strftime("%d/%m/%Y"), inline=True)

    
    if server.icon:
        embed.set_thumbnail(url=server.icon.url)

    
    embed.set_footer(text=f"Demandé par {ctx.author.name}", icon_url=ctx.author.avatar.url)

    
    await ctx.send(embed=embed)

    
















#sondage




votes_utilisateur = {}

@bot.command()
async def sondage(ctx, *, question: str=None):
    if not question:
        await ctx.send(":x: Veuillez entrer le sujet du sondage. Merci !")
        return

  
    embed = discord.Embed(
        title="📊 **Sondage**",
        description=f"**{question}**",
        color=discord.Color.blurple()
    )
    embed.set_footer(text=f"Sondage lancé par {ctx.author.name}", icon_url=ctx.author.avatar.url)

    class SondageView(View):
        def __init__(self):
            super().__init__()
            self.votes = {"Oui": 0, "Non": 0}

        @discord.ui.button(label="Oui", style=discord.ButtonStyle.success, emoji="👍")
        async def vote_oui(self, interaction: discord.Interaction, button: Button):
            if interaction.user.id in votes_utilisateur:
                await interaction.response.send_message(":x: Tu as déjà voté !", ephemeral=True)
                return
            self.votes["Oui"] += 1
            votes_utilisateur[interaction.user.id] = "Oui"
            await interaction.response.send_message("Merci pour ton vote ! 👍", ephemeral=True)

        @discord.ui.button(label="Non", style=discord.ButtonStyle.danger, emoji="👎")
        async def vote_non(self, interaction: discord.Interaction, button: Button):
            if interaction.user.id in votes_utilisateur:
                await interaction.response.send_message(":x: Tu as déjà voté !", ephemeral=True)
                return
            self.votes["Non"] += 1
            votes_utilisateur[interaction.user.id] = "Non"
            await interaction.response.send_message("Merci pour ton vote ! 👎", ephemeral=True)

       
        async def stop_sondage(self):
            return f"**Résultats du sondage :**\n\n👍 **Oui** : {self.votes['Oui']} votes\n👎 **Non** : {self.votes['Non']} votes"

   
    view = SondageView()
    message = await ctx.send(embed=embed, view=view)


    await asyncio.sleep(60)
    view.stop()

    results = await view.stop_sondage()
    await ctx.send(f"Le sondage est terminé !\n{results}")















#avatar


@bot.command()
async def avatar(ctx, member: discord.Member = None):
    if member is None:
        member = ctx.author

    avatar_url = member.display_avatar.url

    
    embed = discord.Embed(
        title=f"🖼️ **Avatar de {member.name}**",
        description=f"Voici l'avatar de {member.mention} !\n\n[Télécharger l'avatar]({avatar_url})",
        color=discord.Color.blurple()
    )
    
   
    embed.set_image(url=avatar_url)

  
    embed.set_footer(text="Bot créé par Pielepoil", icon_url=ctx.bot.user.avatar.url)

    
    await ctx.send(embed=embed)

















# mute








@bot.command()
async def mute_voc(ctx: commands.Context, member: discord.Member, *, reason: str = "Aucune raison donnée"):
    if not member:
        return await ctx.send("❌ **Veuillez mentionner le membre que vous souhaitez mute.**")

    if ctx.guild is None:
        return await ctx.send("❌ Cette commande ne peut pas être utilisée en messages privés.")

    if not ctx.author.guild_permissions.manage_channels:
        return await ctx.send("❌ Vous n'avez pas les permissions nécessaires pour exécuter cette commande.")

    if ctx.author.top_role <= member.top_role:
        return await ctx.send("❌ Vous ne pouvez pas mute ce membre, son rôle est égal ou supérieur au vôtre.")

   
    await member.edit(mute=True, reason=reason)

    embed = discord.Embed(
        title="🔇 **Membre mute dans un canal vocal**",
        description=f"{member.mention} a été mute dans un canal vocal.",
        color=discord.Color.orange()
    )
    embed.set_thumbnail(url="https://emoji.discadia.com/emojis/6d14bd33-33fd-4796-8c60-b3e788f37f4c.png")
    embed.add_field(name="Raison", value=reason, inline=False)
    embed.add_field(name="Modérateur", value=ctx.author.mention, inline=False)
    embed.set_footer(text="Action effectuée avec succès ✅")

    return await ctx.send(embed=embed)

#unmute 

@bot.command()
async def unmute_voc(ctx: commands.Context, member: discord.Member, *, reason: str = "Aucune raison donnée"):
    if not member:
        return await ctx.send("❌ **Veuillez mentionner le membre que vous souhaitez unmute.**")

    if ctx.guild is None:
        return await ctx.send("❌ Cette commande ne peut pas être utilisée en messages privés.")

    if not ctx.author.guild_permissions.manage_channels:
        return await ctx.send("❌ Vous n'avez pas les permissions nécessaires pour exécuter cette commande.")

    if ctx.author.top_role <= member.top_role:
        return await ctx.send("❌ Vous ne pouvez pas unmute ce membre, son rôle est égal ou supérieur au vôtre.")

    
    await member.edit(mute=False, reason=reason)

    embed = discord.Embed(
        title="🔊 **Membre unmute dans un canal vocal**",
        description=f"{member.mention} a été unmute dans un canal vocal.",
        color=discord.Color.green()
    )
    embed.set_thumbnail(url="https://emoji.discadia.com/emojis/6d14bd33-33fd-4796-8c60-b3e788f37f4c.png")
    embed.add_field(name="Raison", value=reason, inline=False)
    embed.add_field(name="Modérateur", value=ctx.author.mention, inline=False)
    embed.set_footer(text="Action effectuée avec succès ✅")

    return await ctx.send(embed=embed)









#ticket




class TicketView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.button(label="Créer un ticket", style=discord.ButtonStyle.green, custom_id="create_ticket_button")
    async def create_ticket(self, interaction: discord.Interaction, button: discord.ui.Button):
        guild = interaction.guild
        user = interaction.user

        
        existing_channel = discord.utils.get(guild.text_channels, name=f"ticket-{user.name.lower()}")
        if existing_channel:
            await interaction.response.send_message("❌ Vous avez déjà un ticket ouvert !", ephemeral=True)
            return

       
        category = guild.get_channel(1306708733728133213)
        if category is None:
            await interaction.response.send_message("⚠️ La catégorie spécifiée pour les tickets est introuvable. Veuillez contacter un administrateur.", ephemeral=True)
            return

        
        overwrites = {
            guild.default_role: discord.PermissionOverwrite(view_channel=False),  
            user: discord.PermissionOverwrite(view_channel=True, send_messages=True, attach_files=True, read_message_history=True),
            guild.me: discord.PermissionOverwrite(view_channel=True, send_messages=True)  
        }

        
        try:
            ticket_channel = await guild.create_text_channel(
                name=f"ticket-{user.name.lower()}",
                category=category,
                overwrites=overwrites,
                reason=f"Ticket créé par {user.name}"
            )
        except discord.Forbidden:
            await interaction.response.send_message("❌ Le bot n'a pas les permissions nécessaires pour créer un canal.", ephemeral=True)
            return
        except discord.HTTPException as e:
            await interaction.response.send_message(f"❌ Une erreur s'est produite lors de la création du ticket : {str(e)}", ephemeral=True)
            return

        await ticket_channel.send(
            content=f"🎫 Bonjour {user.mention}, un membre de l'équipe va bientôt répondre à votre demande. "
                    "Utilisez ce salon pour expliquer votre problème.",
            view=CloseTicketView()
        )
        await interaction.response.send_message(f"✅ Votre ticket a été créé : {ticket_channel.mention}", ephemeral=True)





class CloseTicketView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.button(label="Fermer le ticket", style=discord.ButtonStyle.red, custom_id="close_ticket_button")
    async def close_ticket(self, interaction: discord.Interaction, button: discord.ui.Button):
        channel = interaction.channel

        
        await interaction.response.send_message("⚠️ Ce ticket sera supprimé dans 5 secondes.", ephemeral=True)
        await asyncio.sleep(5)

        try:
            await channel.delete(reason="Ticket fermé par le bouton de fermeture.")
        except discord.Forbidden:
            await interaction.followup.send("❌ Le bot n'a pas les permissions nécessaires pour supprimer ce canal.", ephemeral=True)
        except discord.HTTPException as e:
            await interaction.followup.send(f"❌ Une erreur s'est produite lors de la suppression du ticket : {str(e)}", ephemeral=True)






@bot.command()
async def ticket(ctx):
    """
    Commande pour afficher le message de création de tickets avec le bouton.
    """
    embed = discord.Embed(
        title="Système de Tickets",
        description="Cliquez sur le bouton ci-dessous pour créer un ticket. Un canal privé sera ouvert pour vous permettre de discuter avec l'équipe.",
        color=0x00ff00
    )
    await ctx.send(embed=embed, view=TicketView())









#ban def





@bot.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx: commands.Context, member: discord.Member, *, reason: str = "Aucune raison définie"):

    if not member:
        return await ctx.send("❌ Veuillez mentionner le membre que vous souhaitez bannir.")

    if ctx.guild is None:
        return await ctx.send("❌ Cette commande ne peut pas être utilisée en messages privés.")

    if not ctx.author.guild_permissions.ban_members:
        return await ctx.send("❌ Vous n'avez pas les permissions nécessaires pour bannir ce membre.")

    if ctx.author.top_role <= member.top_role:
        return await ctx.send("❌ Vous ne pouvez pas bannir ce membre, son rôle est égal ou supérieur au vôtre.")
    
    if not ctx.guild.me.guild_permissions.ban_members:
        return await ctx.send("❌ Je n'ai pas les permissions nécessaires pour bannir ce membre.")

    await member.ban(reason=reason)

    
    embed = discord.Embed(
        title="🔨 **Bannissement effectué**",
        description="Un membre a été banni du serveur avec succès !",
        color=discord.Color.red()
    )
    embed.set_thumbnail(url="https://emoji.discadia.com/emojis/6d14bd33-33fd-4796-8c60-b3e788f37f4c.png")
    embed.set_image(url="https://media.giphy.com/media/9J7a2M39nZbxS/giphy.gif") 
    embed.add_field(name="Membre banni", value=f"{member.mention}", inline=True)
    embed.add_field(name="Raison", value=reason, inline=True)
    embed.add_field(name="Modérateur", value=ctx.author.mention, inline=True)
    
    embed.set_footer(text="Action réalisée avec succès ! ✅", icon_url="https://cdn-icons-png.flaticon.com/512/180/180547.png")

    await ctx.send(embed=embed)












#help

bot.help_command = None

@bot.command()
async def help(ctx: commands.Context):
    """
    Commande d'aide affichant les catégories et leurs commandes respectives.
    """

   
    embed_fun = discord.Embed(
        title="🎉 Commandes Fun",
        description="Voici la liste des commandes amusantes disponibles :",
        color=discord.Color.blue()
    )
    embed_fun.set_thumbnail(url="https://cdn-icons-png.flaticon.com/512/1087/1087933.png")
    embed_fun.add_field(
        name="Commandes disponibles (1/2)",
        value=(
            "• **__avatar__** - Affiche votre avatar Discord\n"
            "• **__bingo__** - Jeu où l'on doit trouver un nombre entre 1 et 10\n"
            "• **__blague__** - Raconte une blague\n"
            "• **__battle__** - Bagarre entre 2 membres\n"
            "• **__bouf__** - Donne à manger à un membre\n"
            "• **__compliment__** - Complimente un membre\n"
            "• **__couple__** - Demande de se mettre en couple\n"
            "• **__cat__** - Fournit des photos de chat aléatoires\n"
            "• **__remove_my_couple__** - Vous sépare de votre amour(e)\n"
            "• **__liste_couple__** - Affiche la liste des couples\n"
        ),
        inline=False
    )
    embed_fun.add_field(
        name="Commandes disponibles (2/2)",
        value=(
            "• **__fuck__** - Fait un fuck au membre de votre choix\n"
            "• **__coinflip__** - Jeu du pile ou face\n"
            "• **__dé__** - Lance un dé pour un résultat aléatoire\n"
            "• **__reverse__** - Inverse un texte donné\n"
            "• **__meme__** - Envoie un meme aléatoire\n"
            "• **__love__** - Montre la compatibilité amoureuse ❤️\n"
            "• **__ball8__** - Répond à une question comme une boule magique\n"
            "• **__tu_prefere__** - Propose une question 'tu préfères'\n"
            "• **__luxo_pnj__** - Image d'un gros bot\n"
            "• **__secret_command__** - Fait la et tu verras...\n"
        ),
        inline=False
    )


    embed_moderation = discord.Embed(
        title="🔧 Commandes de Modération",
        description="Commandes réservées aux modérateurs :",
        color=discord.Color.red()
    )
    embed_moderation.add_field(
        name="Commandes disponibles (1/2)",
        value=(
            "• **__ban__** - Bannir définitivement un membre\n"
            "• **__ban_world__** - Bannie le membre de tous les serveurs où le bot est présent\n"
            "• **__kick__** - Expulse un membre du serveur\n"
            "• **__clear__** - Efface un nombre de messages\n"
            "• **__mute__** - Empêche un membre d'envoyer des messages\n"
            "• **__mute_voc__** - Empêche un membre de parler dans un canal vocal\n"
            "• **__unmute__** - Démute un membre précédemment mute\n"
            "• **__unmute_voc__** - Autorise un membre à parler dans un canal vocal\n"
            "• **__banperm__** - Bannir temporairement un utilisateur\n"
        ),
        inline=False
    )
    embed_moderation.add_field(
        name="Commandes disponibles (2/2)",
        value=(
            "• **__warn__** - Avertir un membre pour une infraction\n"
            "• **__liste_warn__** - Liste des avertissements signalés\n"
            "• **__clear_warn__** - Supprime tous les avertissements signalés\n"
            "• **__save_messages__** - Sauvegarde les messages en cas de raid\n"
            "• **__save_configs__** - Sauvegarde les configurations du serveur\n"
            "• **__save_membres__** - Sauvegarde les membres du serveur\n"
            "• **__save_serveur__** - Sauvegarde le serveur\n"
            "• **__nuke__** - Supprime tout le serveur\n"
            "• **__vider_salon__** - Supprime tous les messages d'un salon\n"
        ),
        inline=False
    )

    
    embed_utilities = discord.Embed(
        title="ℹ️ Commandes Utilitaires",
        description="Commandes pour faciliter la gestion et l'information :",
        color=discord.Color.green()
    )
    embed_utilities.add_field(
        name="Commandes disponibles",
        value=(
            "• **__anniv__** - Ajoute votre date d'anniversaire\n"
            "• **__removeanniv__** - Enlève votre anniversaire enregistré\n"
            "• **__ping__** - Affiche le ping du bot\n"
            "• **__serveur_info__** - Informations sur le serveur\n"
            "• **__sondage__** - Crée un sondage ou un vote\n"
            "• **__ticket__** - Crée un ticket de support\n"
            "• **__userinfo__** - Affiche des informations sur un membre\n"
            "• **__uptime__** - Affiche le temps de fonctionnement du bot\n"
            "• **__idee__** - Ajoute une idée pour améliorer le bot !\n"
            "• **__clear_idee__** - Supprime toutes les idées.\n"
            "• **__supp_idee__** - Supprime l'idée de votre choix.\n"
            "• **__liste_idee__** - Liste des idées disponibles.\n"
        ),
        inline=False
    )
    embed_utilities.set_footer(
        text="• Utilisez !<nom de la commande> pour exécuter une commande.",
        icon_url="https://cdn-icons-png.flaticon.com/512/3771/3771492.png"
    )

    
    await ctx.send(embed=embed_fun)
    await ctx.send(embed=embed_moderation)
    await ctx.send(embed=embed_utilities)











# bouf

@bot.command()
async def bouf(ctx, member: discord.Member = None):
    if not member:
        await ctx.send("Veuillez mentionner un membre pour faire cette commande !")
        return
    
    gif_url1 = 'https://media.giphy.com/media/xViO3URQSMj6yCfp9w/giphy.gif?cid=790b761144s6giyrt6zfpkhh2c74yzv7k4jwdrsxtqwhbrqo&ep=v1_gifs_search&rid=giphy.gif&ct=g' 
    gif_url2='https://media.giphy.com/media/iJJ6E58EttmFqgLo96/giphy.gif?cid=ecf05e47lyvthksvj8g0a8wd3pi3ov9yl407dhfkjfw1ffvr&ep=v1_gifs_search&rid=giphy.gif&ct=g'
    gif_url3='https://media.giphy.com/media/QumnfihD4ibhRUqGcH/giphy.gif?cid=790b7611t5xs4pzce05fn0z0i3kz4wabn42eorenkbjs49lt&ep=v1_gifs_search&rid=giphy.gif&ct=g'
    await ctx.send(f"{member.mention}, tu as faim ? Réponds par 'oui' ou 'non' dans les 15 secondes.")

    def check(message):
        return message.author == member and message.content.lower() in ["oui", "non"]

    try:
        reponse = await bot.wait_for('message', check=check, timeout=15.0)

        if reponse.content.lower() == "oui":
            await ctx.send("🎂 Bonne app' !")
            await ctx.send(gif_url1) 
        else:
            await ctx.send("🎉 Dommage... 😔")
            await ctx.send(gif_url2)  

    except asyncio.TimeoutError:
        await ctx.send(f"{member.mention}, tu as pris trop de temps ! 😞")
        await ctx.send(gif_url3)






#fuck





@bot.command()
async def fuck(ctx, member: discord.Member = None):
    
    if not member:
        await ctx.send("❌ **Veuillez mentionner une personne pour utiliser cette commande.**")
        return

    
    embed = discord.Embed(
        title="🔥 Oh, tiens !",
        description=f"{member.mention}, ce message est pour toi ! 😜",
        color=discord.Color.red()
    )
    embed.set_thumbnail(url="https://www.nova.fr/wp-content/thumbnails/uploads/sites/2/2023/11/antesmadzes-t-1352x1348.png")
    embed.set_image(url="https://oranok.wordpress.com/wp-content/uploads/2014/03/doigt-d-honneur-jeune-homme-48-heures-de.jpg")

    embed.set_image(url="https://media.giphy.com/media/3o7aD2saX4glW1uXyo/giphy.gif")  


    
    embed.set_footer(text="Ce message ne doit pas être pris au sérieux, tout est dans l'humour ! 🤪", 
                     icon_url="https://cdn-icons-png.flaticon.com/512/20/20705.png")

    await ctx.send(embed=embed)




#bingo


@bot.command()
async def bingo(ctx):
    nombre_secret = random.randint(1, 10)

    
    embed_lancement = discord.Embed(
        title="🎉 Jeu du Bingo !",
        description="J'ai choisi un nombre entre **1** et **10**. Devine lequel ! (Réponds dans le chat)",
        color=discord.Color.blue()
    )
    embed_lancement.set_footer(text="Tu as 15 secondes pour répondre ! ⏳")
    await ctx.send(embed=embed_lancement)

    def check(message):
        return message.author == ctx.author and message.content.isdigit()

    try:
       
        reponse = await bot.wait_for('message', check=check, timeout=15.0)
        choix = int(reponse.content)

        #
        if choix == nombre_secret:
            embed_victoire = discord.Embed(
                title="🎉 Bravo !",
                description=f"Tu as deviné le bon nombre : **{nombre_secret}** ! Félicitations ! 🎉",
                color=discord.Color.green()
            )
            embed_victoire.set_footer(text="Tu as gagné cette partie ! 😄")
            await ctx.send(embed=embed_victoire)
        else:
            embed_defaite = discord.Embed(
                title="😢 Perdu !",
                description=f"Le bon nombre était **{nombre_secret}**. Essaie encore !",
                color=discord.Color.red()
            )
            embed_defaite.set_footer(text="Ne te décourage pas, tu feras mieux la prochaine fois ! 😉")
            await ctx.send(embed=embed_defaite)
    except asyncio.TimeoutError:
        embed_timeout = discord.Embed(
            title="⏰ Temps écoulé !",
            description=f"Dommage, tu as pris trop de temps ! Le nombre était **{nombre_secret}**.",
            color=discord.Color.orange()
        )
        embed_timeout.set_footer(text="Tu peux toujours essayer à nouveau !")
        await ctx.send(embed=embed_timeout)

















    
    

    

#couple











couples = {}
refus = []

@bot.command()
async def couple(ctx, member2: discord.Member = None):
    member1 = ctx.author  

    
    if not member2:
        await ctx.send("❌ **Tu dois mentionner un(e) membre pour lui proposer de te mettre en couple.**")
        return

    if member1.id == member2.id:
        await ctx.send("😅 **Tu ne peux pas te mettre en couple avec toi-même !**")
        return

    if member1.id in couples or member2.id in couples:
        await ctx.send("❌ **Un des membres est déjà dans un couple !**")
        return

    if member2.id in refus:
        await ctx.send(f"❌ **{member2.mention} a déjà refusé une proposition et ne peut pas être ajouté à un couple.**")
        return

    
    embed_proposition = discord.Embed(
        title="💌 Proposition de Couple",
        description=f"{member1.mention} propose à {member2.mention} de former un couple ! 💕",
        color=discord.Color.purple()
    )
    embed_proposition.set_footer(text="Réponds par 'oui' ou 'non'.")
    await ctx.send(embed=embed_proposition)

    await ctx.send(f"{member2.mention}, acceptes-tu la proposition de {member1.mention} ? Réponds par 'oui' ou 'non'.")

    def check(message):
        return message.author == member2 and message.content.lower() in ['oui', 'non']

    try:
        reponse = await bot.wait_for('message', check=check, timeout=30.0)

        if reponse.content.lower() == 'oui':
            # Ajouter au couple
            couples[member1.id] = member2.id
            couples[member2.id] = member1.id
            embed_felicitation = discord.Embed(
                title="🎉 Félicitations !",
                description=f"{member1.mention} et {member2.mention}, vous êtes officiellement un couple 💕",
                color=discord.Color.dark_purple()
            )
            embed_felicitation.set_footer(text="Profitez bien de votre nouvelle relation !")
            await ctx.send(embed=embed_felicitation)
        else:
            refus.append(member2.id)
            embed_refus = discord.Embed(
                title="😢 Proposition Refusée",
                description=f"{member2.mention} a refusé la proposition de {member1.mention}. Pas de couple cette fois !",
                color=discord.Color.red()
            )
            await ctx.send(embed=embed_refus)

    except asyncio.TimeoutError:
        embed_timeout = discord.Embed(
            title="⏰ Temps écoulé",
            description=f"{member2.mention}, tu as pris trop de temps pour répondre à la proposition de {member1.mention}. 😞",
            color=discord.Color.orange()
        )
        refus.append(member2.id)
        await ctx.send(embed=embed_timeout)


@bot.command()
async def liste_couple(ctx):
    embed = discord.Embed(
        title="💖 Liste des Couples",
        color=discord.Color.pink()
    )

    unique_couples = set()
    if couples:
        couples_text = ""
        for member1_id, member2_id in couples.items():
            if (member2_id, member1_id) not in unique_couples:
                unique_couples.add((member1_id, member2_id))
                member1 = ctx.guild.get_member(member1_id)
                member2 = ctx.guild.get_member(member2_id)
                if member1 and member2:
                    couples_text += f"{member1.mention} et {member2.mention} sont un couple 💕\n"
        embed.add_field(name="❤️ Couples Formés", value=couples_text, inline=False)
    else:
        embed.add_field(name="❤️ Couples Formés", value="Aucun couple formé pour le moment.", inline=False)

    celibataires = [
        member for member in ctx.guild.members
        if member.id not in couples and member.id not in refus and not member.bot
    ]
    if celibataires:
        celibataires_text = "\n".join([member.mention for member in celibataires])
        embed.add_field(name="🧑‍🦰 Célibataires", value=celibataires_text, inline=False)
    else:
        embed.add_field(name="🧑‍🦰 Célibataires", value="Aucun célibataire trouvé.", inline=False)

    if refus:
        refus_text = "\n".join([ctx.guild.get_member(member_id).mention for member_id in refus if ctx.guild.get_member(member_id)])
        embed.add_field(name="😔 Refus", value=refus_text, inline=False)
    else:
        embed.add_field(name="😔 Refus", value="Aucun refus pour le moment.", inline=False)

    await ctx.send(embed=embed)


@bot.command()
async def remove_my_couple(ctx):
    user_id = ctx.author.id

    if user_id not in couples:
        await ctx.send("❌ Tu n'es dans aucun couple pour le moment.")
        return

    partner_id = couples.pop(user_id)
    couples.pop(partner_id)
    partner = ctx.guild.get_member(partner_id)
    embed = discord.Embed(
        title="💔 Fin de Relation",
        description=f"{ctx.author.mention} et {partner.mention} ne sont plus en couple.",
        color=discord.Color.red()
    )
    await ctx.send(embed=embed)




























#anniv






anniversaires = {}


@bot.command()
async def anniv(ctx, date: str = None):
    
    if not date:
        await ctx.send("❌ Veuillez entrer une date au format YYYY-MM-DD. Merci !")
        return

    try:
        
        anniversaire = datetime.strptime(date, '%Y-%m-%d')
        
        
        anniversaires[ctx.author.id] = anniversaire
        
        
        await ctx.send(f":white_check_mark: Ton anniversaire a été enregistré pour le {anniversaire.strftime('%d %B %Y')} ! 🎉")
    except ValueError:
        
        await ctx.send("❌ Le format de la date est invalide. Merci de la saisir sous le format YYYY-MM-DD. N'oublie pas les '-' !")





@bot.command()
async def removeanniv(ctx):
   
    if ctx.author.id in anniversaires:
        del anniversaires[ctx.author.id]
        await ctx.send("😔 Ton anniversaire a été retiré de la liste.")
    else:
        await ctx.send("❌ Tu n'as pas encore enregistré ton anniversaire.")




@tasks.loop(hours=24)  
async def check_anniversaires():
   


    now = datetime.now() 
    for member_id, anniv_date in anniversaires.items():
        
        if anniv_date.month == now.month and anniv_date.day == now.day:
            member = await bot.fetch_user(member_id)
            
            await member.send(f"🎉 Joyeux Anniversaire {member.mention} ! 🎂 Profite de ta journée spéciale ! 🎉")


    check_anniversaires.start() 



















#spam









active_spams = set()


@bot.command()
async def spam(ctx, member: discord.Member, *, message: str = "Repond !!"):
    if member.bot:
        await ctx.send("Je ne peux pas spammer un bot ! 😅")
        return

    spam_key = f"{ctx.guild.id}-{ctx.author.id}-{member.id}"
    if spam_key in active_spams:
        await ctx.send("Un spam est déjà en cours pour cette personne. 😈")
        return

    active_spams.add(spam_key)
    await ctx.send(f"{member.mention}, prépare-toi, je vais te spammer jusqu'à ce que tu répondes ou que quelqu'un écrive 'stop' ! 😈")

    def check_stop_or_reply(msg):
       
        return msg.content.lower() == "stop" or msg.author == member

    async def spam_task():
        while spam_key in active_spams:
           
            await ctx.send(f"{member.mention} {message}")
            await asyncio.sleep(0.5)

    try:
        spammer = asyncio.create_task(spam_task())
        
        await bot.wait_for("message", check=check_stop_or_reply, timeout=60.0)

        
        spammer.cancel()
        if spam_key in active_spams:
            active_spams.remove(spam_key)

        await ctx.send(f"Le spam pour {member.mention} a été arrêté. 😇")

    except asyncio.TimeoutError:
       
        spammer.cancel()
        if spam_key in active_spams:
            active_spams.remove(spam_key)
        await ctx.send(f"{member.mention} n'a pas répondu... 😔 Le spam est arrêté après 60 secondes.")


@bot.command()
async def stop(ctx):
    
    if active_spams:
        active_spams.clear()  
        await ctx.send("Tous les spams ont été arrêtés ! 😇")
    else:
        await ctx.send("Aucun spam en cours à arrêter.")

















#battle













@bot.command()
async def battle(ctx, member2: discord.Member = None):
    member1 = ctx.author

   
    if not member2:
        await ctx.send("❌ **Erreur** : Veuillez mentionner un adversaire pour le combat.")
        return

    
    if member1 == member2:
        await ctx.send("😂 **Impossible** de combattre avec soi-même ! Choisis un autre adversaire.")
        return

    
    await ctx.send(f"⚔️ **Combat proposé !** {member1.mention} défie {member2.mention} !")
    await ctx.send(f"{member2.mention}, acceptes-tu le défi de {member1.mention} ? Réponds par **'oui'** ou **'non'**.")

    
    def check(message):
        return message.author == member2 and message.channel == ctx.channel and message.content.lower() in ['oui', 'non']

    try:
       
        reponse = await bot.wait_for('message', check=check, timeout=30.0)

        if reponse.content.lower() == 'oui':
            
            await ctx.send(f"🎉 Le combat commence entre {member1.mention} et {member2.mention} ! Résultat dans 10 secondes...")

            
            await asyncio.sleep(10)

            
            gagnant = random.choice([member1, member2])
            
            
            embed = discord.Embed(
                title="🏆 Résultat du combat !",
                description=f"Le combat entre {member1.mention} et {member2.mention} est terminé.",
                color=discord.Color.green()
            )
            embed.add_field(name="Le gagnant est...", value=f"**{gagnant.mention}** !", inline=False)
            embed.set_footer(text="Félicitations au champion !")
            await ctx.send(embed=embed)

        else:
            await ctx.send(f"❌ {member2.mention} a refusé de combattre avec {member1.mention}.")

    except asyncio.TimeoutError:
        await ctx.send(f"⏰ {member2.mention}, tu as pris trop de temps pour répondre à la proposition de {member1.mention} ! Le combat est annulé.")






#tu preferes






preferences = [
    "Tu préfères avoir la capacité de voler ou d'être invisible ?",
    "Tu préfères toujours dire la vérité, même si ça blesse, ou mentir pour éviter les conflits ?",
    "Tu préfères manger de la pizza tous les jours ou des sushis tous les jours ?",
    "Tu préfères avoir des pouvoirs de super-héros mais ne pas pouvoir les utiliser ou ne jamais avoir de pouvoirs mais être ultra-intelligent ?",
    "Tu préfères vivre sans musique ou sans films/séries ?",
    "Tu préfères avoir la possibilité de voyager dans le temps ou de lire dans les pensées des autres ?",
    "Tu préfères perdre tous tes souvenirs d'enfance ou ne jamais pouvoir créer de nouveaux souvenirs ?",
    "Tu préfères ne jamais pouvoir utiliser ton téléphone à nouveau ou ne jamais pouvoir utiliser Internet à nouveau ?",
    "Tu préfères avoir un super-pouvoir mais être constamment poursuivi par des méchants, ou être un simple humain mais vivre une vie tranquille ?",
    "Tu préfères être célèbre mais malheureux ou inconnu mais heureux ?",
    "Tu préfères avoir une mémoire parfaite mais perdre la capacité de t'endormir, ou être toujours fatigué mais ne jamais oublier rien ?",
    "Tu préfères vivre dans un monde sans argent ou dans un monde sans guerre ?",
    "Tu préfères rencontrer ton futur moi ou rencontrer ton passé toi ?",
    "Tu préfères être capable de parler toutes les langues du monde ou de jouer de tous les instruments de musique ?",
    "Tu préfères avoir un super-chien qui parle ou un super-chat qui t'aide dans les tâches ménagères ?"
]

@bot.command()
async def tu_prefere(ctx, member: discord.Member = None):
    if not member:
        await ctx.send("❌ **Erreur** : Veuillez mentionner un membre pour lui poser la question !")
        return

   
    question_choisie = random.choice(preferences)

    
    embed = discord.Embed(
        title="🤔 **Question 'Tu préfères'**",
        description=f"{member.mention}, voici une question pour toi :\n\n**{question_choisie}**",
        color=discord.Color.purple()
    )
    embed.set_footer(text=f"Demande faite par {ctx.author.name}", icon_url=ctx.author.avatar.url)

    
    await ctx.send(embed=embed)














#meme aleatoir





API_KEY = "f19oXH4BVSweOkun5A0q8k4i2zedI9Np" 


@bot.command()
async def meme(ctx):
    url = "https://api.giphy.com/v1/gifs/search"
    params = {
        "api_key": API_KEY,
        "q": "funny",  
        "limit": 50    
    }
    
    try:
        
        response = requests.get(url, params=params).json()
        
        if response["data"]:
           
            meme_url = random.choice(response["data"])["images"]["original"]["url"]
            await ctx.send(meme_url)  
        else:
            await ctx.send("❌ Aucun mème trouvé pour cette recherche.")
    except Exception as e:
       
        await ctx.send("❌ Une erreur est survenue en essayant de récupérer un mème.")
        print(f"Erreur : {e}")





#quizz



quizz_questions = [
    {
        "question": "Quel est le plus grand pays du monde par sa superficie ?",
        "choices": ["1) Russie", "2) Canada", "3) Chine", "4) États-Unis"],
        "answer": "1"
    },
    {
        "question": "Combien de continents y a-t-il sur Terre ?",
        "choices": ["1) 5", "2) 6", "3) 7", "4) 8"],
        "answer": "3"
    },
    {
        "question": "Qui a peint la Joconde ?",
        "choices": ["1) Léonard de Vinci", "2) Michel-Ange", "3) Picasso", "4) Monet"],
        "answer": "1"
    },
    {
        "question": "Quelle est la planète la plus proche du Soleil ?",
        "choices": ["1) Vénus", "2) Mercure", "3) Mars", "4) Terre"],
        "answer": "2"
    },
    {
        "question": "Dans quelle ville se trouve la Tour Eiffel ?",
        "choices": ["1) Londres", "2) New York", "3) Paris", "4) Rome"],
        "answer": "3"
    },
    {
        "question": "Combien de jours compte une année bissextile ?",
        "choices": ["1) 364", "2) 365", "3) 366", "4) 367"],
        "answer": "3"
    },
    {
        "question": "Quel est l'élément chimique dont le symbole est 'O' ?",
        "choices": ["1) Or", "2) Oxygène", "3) Osmium", "4) Ozote"],
        "answer": "2"
    },
    {
        "question": "Quelle est la capitale de l'Espagne ?",
        "choices": ["1) Madrid", "2) Barcelone", "3) Séville", "4) Valence"],
        "answer": "1"
    },
    {
        "question": "Combien y a-t-il d'os dans le corps humain adulte ?",
        "choices": ["1) 202", "2) 204", "3) 206", "4) 208"],
        "answer": "3"
    },
    {
        "question": "Quel est le nom du plus long fleuve du monde ?",
        "choices": ["1) Amazone", "2) Nil", "3) Mississippi", "4) Yangzi Jiang"],
        "answer": "1"
    }
]









@bot.command()
async def quiz(ctx):
   
    question = random.choice(quizz_questions)
    
    
    embed = discord.Embed(title="Quiz Time! 🎉", color=discord.Color.blue())
    embed.add_field(name="Question", value=question["question"], inline=False)
    embed.add_field(name="Choix", value="\n".join(question["choices"]), inline=False)
    await ctx.send(embed=embed)

    def check(message):
        
        return message.author == ctx.author and message.channel == ctx.channel and message.content in ["1", "2", "3", "4"]

    try:
        
        response = await bot.wait_for('message', check=check, timeout=15.0)

        if response.content == question["answer"]:
            await ctx.send(f"✅ Bonne réponse, {ctx.author.mention} ! 🎉")
        else:
            await ctx.send(f"❌ Mauvaise réponse... La bonne réponse était : {question['answer']}.")
    
    except asyncio.TimeoutError:
        
        await ctx.send(f"⏰ Temps écoulé, {ctx.author.mention} ! La bonne réponse était : {question['answer']}.")










#ban perm





@bot.command()
@commands.has_permissions(ban_members=True)
async def banperm(ctx, member: discord.Member = None, duration: int = 3600, *, reason=None):
    """
    Commande pour bannir temporairement un membre du serveur.
    :param member: Le membre à bannir.
    :param duration: Durée du ban en secondes (par défaut 3600s, soit 1 heure).
    :param reason: Raison du bannissement.
    """

    if not member:
        await ctx.send("❌ Veuillez mentionner le membre que vous voulez ban.")
        return

    if member == ctx.author:
        await ctx.send("❌ Tu ne peux pas te bannir toi-même !")
        return

    if member.guild_permissions.administrator:
        await ctx.send("❌ Tu ne peux pas bannir un administrateur !")
        return

    if duration <= 0:
        await ctx.send("❌ La durée du bannissement doit être positive !")
        return


    if not ctx.guild.me.guild_permissions.ban_members:
        await ctx.send("❌ Je n'ai pas la permission de bannir des membres !")
        return

    try:
       
        await member.ban(reason=reason)
        await ctx.send(f"🚫 {member.mention} a été banni pour {duration} secondes. Raison : {reason or 'Aucune raison spécifiée'}")

        
        await asyncio.sleep(duration)

        
        await ctx.guild.unban(member)
        await ctx.send(f"✅ {member.mention} a été débanni après {duration} secondes.")
    
    except Exception as e:
        await ctx.send(f"❌ Une erreur est survenue : {e}")









#cat




@bot.command()
async def cat(ctx):
    url =  "https://api.thecatapi.com/v1/images/search"
    reponse = requests.get(url).json()
    await ctx.send(reponse[0]["url"])









#avertissement 

avertissements = {}

@bot.command()
@commands.has_permissions(kick_members=True)
async def warn(ctx, member: discord.Member = None, *, reason: str = None):
    """
    Commande pour avertir un membre.
    :param member: Le membre à avertir.
    :param reason: La raison de l'avertissement.
    """
    if not member:
        await ctx.send("❌ Veuillez mentionner un membre à avertir.")
        return

    if not reason:
        await ctx.send("❌ Veuillez fournir une raison pour l'avertissement.")
        return

    
    if member.id not in avertissements:
        avertissements[member.id] = []

    avertissements[member.id].append(reason)

    nb_avertissements = len(avertissements[member.id])
    await ctx.send(f"⚠️ {member.mention} a été averti pour : {reason}")
    await ctx.send(f"ℹ️ {member.mention} a maintenant {nb_avertissements} avertissement(s).")

    
    if nb_avertissements >= 3:
        await member.kick(reason="Nombre d'avertissements dépassé.")
        await ctx.send(f"🚨 {member.mention} a été kické après {nb_avertissements} avertissement(s).")






@bot.command()
async def liste_warn(ctx):
    """
    Commande pour lister tous les avertissements.
    """
    if not avertissements:
        await ctx.send("📭 Aucun avertissement n'a été enregistré pour le moment.")
        return

    messages = []
    for member_id, reasons in avertissements.items():
        user = await bot.fetch_user(member_id)
        liste_raisons = "\n    ".join([f"- {reason}" for reason in reasons])
        messages.append(f"👤 **{user}** :\n    {liste_raisons}")


    for i in range(0, len(messages), 5):  
        bloc = "\n\n".join(messages[i:i + 5])
        await ctx.send(f"📋 **Liste des avertissements :**\n{bloc}")









@bot.command()
@commands.has_permissions(kick_members=True)
async def clear_warn(ctx, member: discord.Member = None):
    """
    Commande pour effacer les avertissements d'un membre ou de tout le monde.
    """
    if not member:
        avertissements.clear()
        await ctx.send("🧹 Tous les avertissements ont été effacés.")
    else:
        if member.id in avertissements:
            del avertissements[member.id]
            await ctx.send(f"✅ Les avertissements de {member.mention} ont été effacés.")
        else:
            await ctx.send(f"ℹ️ {member.mention} n'a aucun avertissement enregistré.")
















#kick

@bot.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member = None, *, reason: str = None):
    
    if not member:
        await ctx.send("⚠️ **Veuillez mentionner un membre que vous souhaitez expulser.**")
        return

    
    if not reason:
        await ctx.send("⚠️ **Veuillez entrer une raison pour l'expulsion.**")
        return

   
    await member.kick(reason=reason)

   
    embed = discord.Embed(
        title="⚡ **Expulsion réussie**", 
        description=f"{member.mention} a été expulsé du serveur.", 
        color=discord.Color.red() 
    )
    embed.add_field(name="**Raison de l'expulsion :**", value=f"_{reason}_", inline=False)
    embed.set_footer(text=f"Action effectuée par {ctx.author.name}", icon_url=ctx.author.avatar.url)

    
    await ctx.send(embed=embed)





#uptime






@bot.command()
async def uptime(ctx):
    """
    Commande pour afficher la durée pendant laquelle le bot est en ligne.
    """
    if not hasattr(bot, "launch_time"):
        await ctx.send("❌ Impossible de calculer l'uptime. L'heure de lancement n'est pas définie.")
        return

    delta_uptime = discord.utils.utcnow() - bot.launch_time
    
    days, seconds = delta_uptime.days, delta_uptime.seconds
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    seconds = seconds % 60

    uptime_message = f"🕒 Le bot est en ligne depuis : {days} jours, {hours} heures, {minutes} minutes et {seconds} secondes."
    await ctx.send(uptime_message)













# dées





@bot.command()
async def dé(ctx):
    
    url_1 = "https://media.giphy.com/media/3ov9kacqGycKQRH6Vy/giphy.gif?cid=790b7611whyaqi8i4ndcex7aadjm8voyphsq2p1swhnv3r4n&ep=v1_gifs_search&rid=giphy.gif&ct=g"
    url_2 = "https://media.giphy.com/media/l378wGtG2aQgZJT32/giphy.gif?cid=790b76112wz2qv40c4m934as5zmsz8wbdf37mkujh3hy51es&ep=v1_gifs_search&rid=giphy.gif&ct=g"
    url_3 = "https://media.giphy.com/media/3ov9kaW3wyiefU3GGA/giphy.gif?cid=790b76118xtrhzyizpykfadg8x7ol2ny739hluo2uxcq08t7&ep=v1_gifs_search&rid=giphy.gif&ct=g"
    url_4 = "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExODNnNWhmaGc5NDZxNGc5eGw0aXFteGh5Mm12ZDdwMWhoNWF6eDkxbiZlcD12MV9naWZzX3NlYXJjaCZjdD1n/jSEFUIq3EE4oyX2Be4/giphy.gif"
    url_5 = "https://media.giphy.com/media/7iPKtEjz5z2xycRPF3/giphy.gif?cid=ecf05e47drrtoypuncin19q2ajmnpazq94eeugqukerv86hi&ep=v1_gifs_search&rid=giphy.gif&ct=g"
    url_6 = "https://media.giphy.com/media/L4NtmZmGB6zwUKPw6R/giphy.gif?cid=790b7611lolzsk4aaixw42d17aeuw0mh3032bl8rwmsjoi7q&ep=v1_gifs_search&rid=giphy.gif&ct=g"

   
    result = random.randint(1, 6)

    
    if result == 1:
        gif_url = url_1
    elif result == 2:
        gif_url = url_2
    elif result == 3:
        gif_url = url_3
    elif result == 4:
        gif_url = url_4
    elif result == 5:
        gif_url = url_5
    else:
        gif_url = url_6

    
    await ctx.send(f"Tu as lancé un dé. Le résultat est {result}! 🎲")
    await ctx.send(gif_url)






#comtabilité amoureuse 






@bot.command()
async def love(ctx, member: discord.Member = None):
    
    if member is None:
        await ctx.send("Veuillez mentionner un membre pour vérifier votre compatibilité amoureuse ! 💕")
        return

    
    if member.id == ctx.author.id:
        await ctx.send("Vous ne pouvez pas tester votre compatibilité amoureuse avec vous-même. 🙃")
        return

    
    compatibility = random.randint(1, 100)

    
    if compatibility > 75:
        emoji = "💘"
        message = "Vous êtes faits l'un pour l'autre ! 🥰"
    elif compatibility > 50:
        emoji = "❤️"
        message = "Vous avez une bonne alchimie. 💕"
    elif compatibility > 25:
        emoji = "💔"
        message = "Ce n'est pas gagné, mais il y a de l'espoir. 🤔"
    else:
        emoji = "😢"
        message = "Ouch... l'amour ne semble pas au rendez-vous. 😓"

    
    await ctx.send(
        f"{ctx.author.mention} et {member.mention} ont {compatibility}% de compatibilité amoureuse ! {emoji}\n{message}"
    )










#reverse


@bot.command()
async def reverse(ctx, *, text: str):
    reversed_text = text[::-1]
    await ctx.send(f"Texte inversé : {reversed_text}")





#8 ball


@bot.command()
async def ball8(ctx, *, question: str = None):
    if not question:
        await ctx.send("Veuillez entrer une question. Merci !")
        return

    
    responses = [
        "Oui.",
        "Non.",
        "Peut-être.",
        "C'est certain.",
        "Je ne sais pas.",
        "Demande plus tard."
    ]

    
    response = random.choice(responses)

    
    embed = discord.Embed(
        title="🔮 **Boule Magique**", 
        description=f"Voici la réponse à ta question, {ctx.author.mention} !", 
        color=discord.Color.purple() 
    )
    embed.add_field(name=f"**Question :**", value=f"_{question}_", inline=False)
    embed.add_field(name="**Réponse :**", value=f"**{response}**", inline=False)
    
    
    embed.set_thumbnail(url="https://cdn-icons-png.flaticon.com/512/2520/2520855.png")
    embed.set_footer(text="La boule magique ne ment jamais... ou presque.")

    await ctx.send(embed=embed)


#luxo








@bot.command()
async def luxo_pnj(ctx):
    
    urls = [
        'https://cdn.discordapp.com/attachments/1269055563212394509/1303758891485495498/image.png?ex=673f6096&is=673e0f16&hm=979024cfab1c77f2d49ef7af4297ad6aea8164aaf7d6d180a46190a6c082ca51&',
        'https://cdn.discordapp.com/attachments/1269055563212394509/1303758078520332359/IMG_0231.png?ex=67400894&is=673eb714&hm=0fa13fbbd618a849efb36ddfc3e83c7f4887139ce4b5b605ed5b049a6cf44505&',
        'https://media.discordapp.net/attachments/1269055563212394509/1303758076331167876/IMG_0240.png?ex=67400894&is=673eb714&hm=eadd1b9e93c126888a559e225bbd92dcc294c46a6b1cb70999da6254c6b5d438&=&format=webp&quality=lossless',
        'https://cdn.discordapp.com/attachments/1269055563212394509/1305913682299191337/Opera_Instantane_2023-11-30_052348_www.tiktok.com.png?ex=673ff724&is=673ea5a4&hm=c887aa90753c1cbc0ec6e4e693a4ca89864aafaafcca4495fd3b829a048fa3d7&',
        'https://cdn.discordapp.com/attachments/1269055563212394509/1303758106907512832/IMG_0227.png?ex=6740089b&is=673eb71b&hm=af6089f6a8b97d868e1e9854f31cc602c52f43a9a102178631e0cf4b3009bcb8&',
        'https://cdn.discordapp.com/attachments/1269055563212394509/1292281434492506153/Capture_decran_2024-10-06_022352.png?ex=6740781f&is=673f269f&hm=61a761b7d9745ee1d42b2b928a41c126902fbbefb8b6d721bad9dbfa9448ca5a&',
        'https://cdn.discordapp.com/attachments/1269055563212394509/1303758077128085605/IMG_0238.png?ex=67400894&is=673eb714&hm=73abf79ce06ba9d608fb1eb639c7d8c06143bab560538a7addf56501f20e4158&'
    ]

    
    random_url = random.choice(urls)

    embed = discord.Embed()
    embed.set_image(url=random_url)  

    
    await ctx.send(embed=embed)




#vider salon





@bot.command()
async def vider_salon(ctx):
    
    
    if not ctx.author.guild_permissions.manage_messages:
        await ctx.send(":x: Désolé, vous n'avez pas les permissions nécessaires pour utiliser cette commande.")
        return

    
    deleted = await ctx.channel.purge()

   
    embed = discord.Embed(
        title="🗑️ Salon vidé avec succès",
        description=f"{len(deleted)} messages ont été supprimés dans ce salon.",
        color=discord.Color.green()
    )
    embed.set_footer(text=f"Commande effectuée par {ctx.author.name}", icon_url=ctx.author.avatar.url)
    
    
    await ctx.send(embed=embed)










@bot.command()
async def save_serveur(ctx, channel: discord.TextChannel = None):
    
    
    await ctx.send("Commande en cours... Cela peut prendre quelques secondes.")

   
    if not channel:
        channel = ctx.channel

   
    messages = []
    async for message in channel.history(limit=1000):
        messages.append(f"{message.author}: {message.content}\n")

    messages_file = f"sauvegarde_messages_{channel.name}.txt"
    with open(messages_file, "w", encoding="utf-8") as f:
        f.writelines(messages)

    
    members_info = []
    for member in ctx.guild.members:
        members_info.append({
            "nom": member.name,
            "roles": [role.name for role in member.roles],
            "status": str(member.status)
        })

    members_file = f"sauvegarde_membres_{time.strftime('%Y%m%d-%H%M%S')}.txt"
    with open(members_file, "w", encoding="utf-8") as f:
        for member in members_info:
            f.write(f"Nom: {member['nom']}\n")
            f.write(f"Rôles: {', '.join(member['roles'])}\n")
            f.write(f"Statut: {member['status']}\n\n")

   
    channels_info = {
        channel.name: {
            "id": channel.id,
            "type": str(channel.type),
            "position": channel.position
        }
        for channel in ctx.guild.channels
    }

    roles_info = {
        role.name: {
            "id": role.id,
            "permissions": [perm[0] for perm in role.permissions if perm[1]],
            "color": str(role.color)
        }
        for role in ctx.guild.roles
    }

    config_data = {"channels": channels_info, "roles": roles_info}
    config_file = "sauvegarde_configuration.json"
    with open(config_file, "w", encoding="utf-8") as f:
        json.dump(config_data, f, indent=4)

   
    embed = discord.Embed(
        title="💾 Sauvegarde complète du serveur",
        description="Les informations suivantes ont été sauvegardées avec succès :",
        color=discord.Color.green()
    )
    embed.add_field(name="Messages", value=f"{len(messages)} messages sauvegardés.", inline=False)
    embed.add_field(name="Membres", value=f"{len(members_info)} membres sauvegardés.", inline=False)
    embed.add_field(name="Configuration", value="Paramètres du serveur sauvegardés.", inline=False)

    await ctx.send(embed=embed)
    
    await ctx.send(f"Les derniers messages de {channel.mention} ont été sauvegardés :", file=discord.File(messages_file))
    await ctx.send(f"Les informations des membres ont été sauvegardées :", file=discord.File(members_file))
    await ctx.send(f"La configuration du serveur a été sauvegardée :", file=discord.File(config_file))

   
    os.remove(messages_file)
    os.remove(members_file)
    os.remove(config_file)









#save message 





@bot.command()
async def save_messages(ctx, channel: discord.TextChannel = None):
   
    if not ctx.author.guild_permissions.manage_messages:
        embed = discord.Embed(
            title="⛔ Accès refusé",
            description="Tu n'as pas la permission de sauvegarder les messages de ce canal.",
            color=discord.Color.red()
        )
        await ctx.send(embed=embed)
        return

   
    if not channel:
        channel = ctx.channel

    
    messages = []
    async for message in channel.history(limit=1000):
        messages.append(f"{message.created_at} - {message.author}: {message.content}\n")

  
    if not messages:
        embed = discord.Embed(
            title="🔒 Aucune donnée",
            description=f"Aucun message à sauvegarder dans {channel.mention}.",
            color=discord.Color.orange()
        )
        await ctx.send(embed=embed)
        return

    
    file_name = f"sauvegarde_messages_{channel.name}.txt"
    try:
        with open(file_name, "w", encoding="utf-8") as f:
            f.writelines(messages)

        
        embed = discord.Embed(
            title="💾 Sauvegarde réussie",
            description=f"Les derniers messages de {channel.mention} ont été sauvegardés avec succès.",
            color=discord.Color.green()
        )
        embed.add_field(name="Canal", value=channel.mention, inline=True)
        embed.add_field(name="Nombre de messages", value=len(messages), inline=True)
        await ctx.send(embed=embed, file=discord.File(file_name))

    finally:
        
        if os.path.exists(file_name):
            os.remove(file_name)










#save membre





@bot.command()
async def save_membres(ctx):
    
    if not ctx.author.guild_permissions.administrator:
        embed = discord.Embed(
            title="⛔ Accès refusé",
            description="Tu n'as pas les permissions nécessaires pour sauvegarder les informations des membres.",
            color=discord.Color.red()
        )
        await ctx.send(embed=embed)
        return

   
    members_info = []
    for member in ctx.guild.members:
        member_info = {
            "nom": member.name,
            "role": [role.name for role in member.roles],
            "status": str(member.status).capitalize()
        }
        members_info.append(member_info)

    
    timestamp = time.strftime("%Y%m%d-%H%M%S")
    file_name = f"sauvegarde_membres_{timestamp}.txt"

    
    with open(file_name, "w", encoding="utf-8") as f:
        for member in members_info:
            f.write(f"Nom: {member['nom']}\n")
            f.write(f"Rôles: {', '.join(member['role'])}\n")
            f.write(f"Statut: {member['status']}\n\n")

    
    embed = discord.Embed(
        title="💾 Sauvegarde réussie",
        description=f"Les informations des membres du serveur ont été sauvegardées avec succès.",
        color=discord.Color.green()
    )
    embed.add_field(name="Nombre de membres sauvegardés", value=len(members_info), inline=True)
    embed.set_footer(text=f"Sauvegardé par {ctx.author.name}", icon_url=ctx.author.avatar.url)

    await ctx.send(embed=embed, file=discord.File(file_name))

    
    os.remove(file_name)












#sauvegarde config 




@bot.command()
async def save_configs(ctx):
    if not ctx.author.guild_permissions.administrator:
        embed = discord.Embed(
            title="⛔ Accès refusé",
            description="Tu n'as pas la permission de sauvegarder la configuration du serveur.",
            color=discord.Color.red()
        )
        await ctx.send(embed=embed)
        return

    
    channels_info = {}
    for channel in ctx.guild.channels:
        channels_info[channel.name] = {
            "id": channel.id,
            "type": str(channel.type),
            "position": channel.position
        }

    
    roles_info = {}
    for role in ctx.guild.roles:
        roles_info[role.name] = {
            "id": role.id,
            "permissions": [perm[0] for perm in role.permissions if perm[1]],
            "color": str(role.color)
        }

    
    config_data = {
        "channels": channels_info,
        "roles": roles_info
    }

    
    file_name = "sauvegarde_configuration.json"
    with open(file_name, "w", encoding="utf-8") as f:
        json.dump(config_data, f, indent=4)

    
    embed = discord.Embed(
        title="✅ Sauvegarde réussie",
        description="La configuration du serveur a été sauvegardée avec succès. Voici le fichier.",
        color=discord.Color.green()
    )
    embed.set_footer(text=f"Sauvegardé par {ctx.author.name}")
    
    await ctx.send(embed=embed, file=discord.File(file_name))

    
    os.remove(file_name)





#nuke



@bot.command()
async def nuke(ctx):
   
    if not ctx.author.guild_permissions.administrator:
        embed = discord.Embed(
            title="⛔ Accès refusé",
            description="Tu n'as pas les permissions pour effectuer cette action. Seul un administrateur peut lancer cette commande.",
            color=discord.Color.red()
        )
        await ctx.send(embed=embed)
        return

    
    embed = discord.Embed(
        title="⚠️ Alerte de suppression",
        description="Es-tu sûr de vouloir supprimer tout le serveur ? Cette action est irréversible.\nTape 'oui' pour confirmer.",
        color=discord.Color.orange()
    )
    await ctx.send(embed=embed)

    def check(message):
        return message.author == ctx.author and message.content.lower() == 'oui'

    try:
        
        confirmation = await bot.wait_for('message', check=check, timeout=60.0)
    except asyncio.TimeoutError:
        embed = discord.Embed(
            title="⏰ Temps écoulé",
            description="Le délai est dépassé. Action annulée.",
            color=discord.Color.red()
        )
        await ctx.send(embed=embed)
        return

    
    embed = discord.Embed(
        title="🗑️ Suppression des messages",
        description="Suppression de tous les messages dans les salons de texte en cours...",
        color=discord.Color.green()
    )
    await ctx.send(embed=embed)
    for channel in ctx.guild.text_channels:
        await channel.purge()

  
    embed = discord.Embed(
        title="🗑️ Suppression des rôles",
        description="Suppression de tous les rôles (excepté @everyone) en cours...",
        color=discord.Color.green()
    )
    await ctx.send(embed=embed)
    for role in ctx.guild.roles:
        if role.name != "@everyone":
            await role.delete()

    
    embed = discord.Embed(
        title="🗑️ Suppression des membres",
        description="Suppression des membres (kick) en cours...",
        color=discord.Color.green()
    )
    await ctx.send(embed=embed)
    for member in ctx.guild.members:
        if not member.bot and member != ctx.author:
            try:
                await member.kick(reason="🗑️ Suppression complète du serveur")
            except discord.Forbidden:
                await ctx.send(f"🗑️ Je n'ai pas la permission de kick {member.name}.")
                continue

    
    embed = discord.Embed(
        title="🗑️ Suppression des salons",
        description="Suppression de tous les salons du serveur en cours...",
        color=discord.Color.green()
    )
    await ctx.send(embed=embed)
    for channel in ctx.guild.channels:
        await channel.delete()

    
    embed = discord.Embed(
        title="💥 Le serveur a été supprimé",
        description=f"Toutes les données du serveur {ctx.guild.name} ont été effacées. Le serveur est désormais vide.",
        color=discord.Color.red()
    )
    await ctx.send(embed=embed)

    embed = discord.Embed(
        title="✅ Suppression terminée",
        description="Tout le serveur a été supprimé avec succès.",
        color=discord.Color.green()
    )
    await ctx.send(embed=embed)
























@bot.command()
async def secret_command(ctx):
    await ctx.send("zIl il a une commande cacher sur le serveur, a vous de la trouver pour __e__ obtenir une recompense bonnus. PS : j'ai cacher des indices dans le serve**u**r **b**onne chance ^^||pas la||")
























url = 'https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExaHM2OWJ3NTdnbzVxbHp0Zzgwc2huemw5OWNjajY3dWtqaXowMmJjbyZlcD12MV9naWZzX3NlYXJjaCZjdD1n/Ju7l5y9osyymQ/giphy.gif'

class TicketView(discord.ui.View):
    def __init__(self, ctx):
        super().__init__()
        self.ctx = ctx 

    @discord.ui.button(label="Clique ici", style=discord.ButtonStyle.green)
    async def troll(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message(
            content="Haha, tu as été trollé ! 🎉",
            ephemeral=True,
        )
        await self.ctx.send(f"{url}")

@bot.command()
async def zeub(ctx):
    embed = discord.Embed(
        title="Clique pour recevoir ton gain",
        description="Cliquez sur le bouton ci-dessous. Bravo !",
        color=0x00ff00
    )
    await ctx.send(embed=embed, view=TicketView(ctx))  









#idee pour le bot 






if os.path.exists("idees.json"):
    try:
        with open("idees.json", "r") as f:
            idées = json.load(f)
    except json.JSONDecodeError:
        print("⚠️ Erreur : le fichier 'idees.json' est corrompu. Réinitialisation de la liste des idées.")
        idées = []
else:
    idées = []


def save_ideas():
    with open("idees.json", "w") as f:
        json.dump(idées, f)


@bot.command()
async def idee(ctx, *, idee_user: str = None):  
    if not idee_user: 
        await ctx.send("❌ Veuillez entrer une idée après la commande. Exemple : `!idee Mon idée géniale`.")
        return

    idee_user = idee_user.strip() 

    
    if idee_user.lower() in (idee.lower() for idee in idées):
        await ctx.send(f"❌ Cette idée '{idee_user}' a déjà été proposée.")
        return

    idées.append(idee_user) 
    save_ideas()  
    await ctx.send(f"✅ Votre idée '{idee_user}' a bien été ajoutée !")








#liste idee
@bot.command()
async def liste_idee(ctx):
    if not idées:
        await ctx.send("📭 Aucune idée n'a été proposée pour le moment.")
    else:
        bloc_size = 10  
        for i in range(0, len(idées), bloc_size):
            bloc = idées[i:i + bloc_size]
            liste_complete = "\n".join(f"- {idee}" for idee in bloc)
            await ctx.send(f"📋 **Idées proposées :**\n{liste_complete}")






#supp idee
@bot.command()
async def supp_idee(ctx, *, idee_user: str = None):
    if not idee_user:
        await ctx.send("❌ Veuillez spécifier l'idée à supprimer. Exemple : `!supprime_idee Mon idée géniale`.")
        return

    idee_user = idee_user.strip()

    if idee_user in idées:
        idées.remove(idee_user)  
        save_ideas()  
        await ctx.send(f"🗑️ L'idée '{idee_user}' a été supprimée.")
    else:
        await ctx.send(f"❌ L'idée '{idee_user}' n'existe pas dans la liste.")

#supp all idee




@bot.command()
async def clear_idees(ctx):
    idées.clear()  
    save_ideas()  
    await ctx.send("🧹 Toutes les idées ont été supprimées.")
















#gestion ereure



@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("❌ Argument manquant dans la commande. Veuillez vérifier et réessayer.")
    elif isinstance(error, commands.CommandNotFound):
        await ctx.send("❌ Commande inconnue. Tapez `!help` pour voir la liste des commandes disponibles.")
    else:
        print(f"Une erreur inattendue s'est produite : {error}")
        await ctx.send("⚠️ Une erreur inattendue s'est produite. Veuillez réessayer.")
































#all info user



@bot.command()
async def userinfo(ctx, member: discord.Member = None):
    
    if not member:
        await ctx.send("Veuillez mentionner un membre pour obtenir ses informations.")
        return

    
    name = member.name
    discriminator = member.discriminator
    user_id = member.id
    joined_at = member.joined_at.strftime("%d/%m/%Y, %H:%M:%S")
    created_at = member.created_at.strftime("%d/%m/%Y, %H:%M:%S")
    status = str(member.status).capitalize()
    activity = str(member.activity) if member.activity else "Aucune activité"
    roles = [role.name for role in member.roles if role.name != "@everyone"]

   
    embed = discord.Embed(
        title=f"Informations sur {name}",
        description=f"Voici les informations détaillées de **{name}**",
        color=discord.Color.blue()
    )
    embed.set_thumbnail(url=member.avatar.url)  
    embed.set_footer(text=f"ID du membre: {user_id}")

    
    embed.add_field(name="Nom", value=name, inline=True)
    embed.add_field(name="Discriminant", value=f"#{discriminator}", inline=True)
    embed.add_field(name="Statut", value=status, inline=True)
    embed.add_field(name="Activité", value=activity, inline=False)
    embed.add_field(name="Rôles", value=", ".join(roles), inline=False)
    embed.add_field(name="Date d'adhésion", value=joined_at, inline=True)
    embed.add_field(name="Date de création", value=created_at, inline=True)

    
    await ctx.send(embed=embed)





TOKEN = 'your token'

bot.run(TOKEN)

