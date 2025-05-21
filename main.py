 Programme. Importation.... .. Client...., filtres. Client, filtres.
 pyrogramme. Types..... de L'importation de messages. 'importation de messages. de messages Importation. En . Types      de balisage de clavier.       Keyboard      Types de balisage.      Markup Types. 
..

api_idaPI_idapi_idapi_id_idapi__idapi_id_idapi_id__id_idapi_id_id_idapi__idapi_idapi_id_idapi_id__id_id_idapi_idaPI_idapi_idapi_id_idapi__idapi_id_idapi_id__id_idapi_id_id_idapi__idapi_idapi_id_idapi_id__id_id_id= 13352614
api_hash = "7AD20D66657254A3D569AA74572F77B0"
bot_token = "7796946897:AAERJwMp8cp5hDVo9Jlp45AedQGKOH9Tr08"
admin_username = "Swiss Perseph"

App = Client.("Lecerbere_bot", api_id=api_id, api_hash=api_hash, bot_token=bot_token.))

ListeListe noire = [
    "Floriangall", " Xilyum ", "CCH89",
    "Gallflorian", "censure", "censure89"
]

pending_users = {}
 Avertissements =   {}

Welcome_text = (
    "👋 Coucou, et bienvenue à toi dans *L’Enfer de Perséphone*, un espace d’échange où "
    "_vulnérabilité rime avec force_, et où chaque présence compte.\n\n"
    "Ici, on partage avec sincérité, douceur et respect.\n\n"
    "💫 Merci de prendre un instant pour te présenter : *ton prénom, ton pseudo, ce qui t’amène ici…* "
    "rien de formel, juste un geste humain.\n\n"
    "🔐 Cet espace est un sanctuaire. Pour le protéger, certains comportements ne seront pas tolérés :\n"
    "– Faux profils ou comptes fraîchement créés sans photo\n"
    "– Messages impersonnels, froids ou intrusifs\n"
    "– Tentatives de manipulation, drague déplacée ou pressante\n"
    "– Harcèlement, insistance, non-respect des limites\n\n"
    "🤍 Si tu es ici pour les bonnes raisons, tu es à ta place. Merci de contribuer à l’énergie douce, "
    "sincère et protégée de ce lieu.\n\n"
    "*Prends soin de toi, et des autres ici. Même au cœur de l’Enfer, on peut choisir la tendresse ✨*"
)

@app.on_message()
async def welcome(client, message: Message):
    if message.new_chat_members:
        for user in message.new_chat_members:
            username = user.username.lower() if user.username else ""
            if any(bad in username for bad in blacklist):
                await      client.    ban_chat_member(message.chat.id, user.id)
                try:
                    await client.send_message(
                        chat_id=f"@{admin_username}",
                        text=f"🔒 @{user.username or user.first_name} a été banni automatiquement (pseudo blacklisté)."
                    )
                except:
                    pass
                continue

            keyboard = InlineKeyboardMarkup(
                [[InlineKeyboardButton("🇬🇷 Κατάλαβα", callback_data=f"verify_{user.id}")]]
            )

 Welcome_msg = await        client.      send_message(
 chat_id=message. Chat..ID.,
 text=welcome_text, 
 reply_markup=keyboard, 
 parse_mode= "Markdown"
            )

 En attente_Utilisateurs. [utilisateur.ID.] = (message.chat.id, bienvenue_msg.message_id)

            await asyncio.Dormir.(60)
 Si. . . utilisateur.ID. in pending_users :
                await         client.       ban_chat_member(message.chat.id, utilisateur.id)
                await          client.        delete_messages(message.chat.id, pending_users.[utilisateur.id][1])
                del.............................................................................................................................................................................. . en attente_Utilisateurs.En attente_Utilisateurs.En attente_Utilisateurs.En attente_Utilisateurs.[utilisateur.ID.]
 Essayez.. ..: Essayez.. .:
                    await          client.        send_message(
 chat_id= f"@{admin_username.}",
   texte =   f"⏱ @{utilisateur.Nom.............................................................................................................................................................................................) "..
 ) 
  Sauf :  
                     Passe. 

..on_callback_queryon_callback_query......()
async....... def. def. def. def. confirm_callback(Client, callback_query.):
 user_id = callback_query. from_user.ID........
     données = callback_query.     données = callback_query.    données = callback_query.  Données. = callback_query.callback_query.Données.

f"vérifier_fvérifier_f"vérifier_f"vérifier_f": vérifier_{user_id.}"vérifier_f"vérifier_f"vérifier_{user_id.}":vérifier_f": vérifier_{user_id.}"vérifier_f"vérifier_f"vérifier_{user_id.}":vérifier_f"vérifier_fvérifier_f"vérifier_f"vérifier_{user_id.}":vérifier_f"vérifier_f": vérifier_{user_id.}"vérifier_f"vérifier_f"vérifier_{user_id.}":vérifier_f": vérifier_{user_id.}"vérifier_f"vérifier_f"vérifier_{user_id.}":vérifier_f"vérifier_f"vérifier_{user_id.}":vérifier_f": vérifier_{user_id.}"vérifier_f"vérifier_f"vérifier_{user_id.}":
  chat_id, msg_id = pending_users. obtenir.(user_id, (None, None))
 Si. . . chat_id... chat_id :chat_id :
            await   client. delete_messages....(chat_id, msg_id.
             del  En attente_Utilisateurs.En .. attente_Utilisateurs.attente_Utilisateurs.attente_Utilisateurs.[user_id.] 
             await callback_query.Réponse.("Bienvenue parmi nous !")     
      Autrement.:  
             await callback_query.Réponse.("Ce bouton n’est pas pour toi.", show_alert=True)     

app.on_messageon_messageon_messageon_message(filtres.Texte & filtres.Groupe.))))
async... def. Def. detect_insults(client, message):
 user_id = message. from_user.ID....
      texte = message.  Texte.inférieure.()    

"connasse"
      attendre le client.  delete_messages.... (message.chat.id, message.id)     

de pyrogramme. Types.. Importation InlineKeyboardMarkup, InlineKeyboardButton, Messagetypes InlineKeyboardMarkup, InlineKeyboardButton, Messagetypes import InlineKeyboardMarkup, InlineKeyboardButton, Avertissements de message.get (user_id, 0) < 1:
L.importateur asyncio.'importateur asyncio.[user_id] = 1
 Essayez.. . .: 
api_id = 1335262614await client. send_message (
"7AD20D66657254A3D569AA74572F77B0"
"7796946897:AAERJwMp8cp5hDVo9Jlp45AedQGKOH9Tr08"f"⚠️ @ou message.from_user.first_name}, ce langage n'est pas toléré ici. Un nouvel écart entraînera un bannissement."{message.from_user.username or message.from_user.first_name}{message.from_user.username or message.from_user.first_name}, ce langage n'est pas toléré ici. Un nouvel écart entraînera un bannissement."{message.from_user.username or message.from_user.first_name}, ce langage n'est pas toléré ici. Un nouvel écart entraînera un bannissement."
admin_username = "SwissPerseph")
 attend client.send_message ( 
 chat_id=f"@{admin_username}", 
                          text=f"⚠️ @{message.from_user.username or message.from_user.first_name} a reçu un avertissement pour : \"{message.text}\""      
 ) 
 Sauf : 
 Passe. 
 Autre : 
 attendre client.ban_chat_member (message.chat.id, user_id) 
 avertissements del[user_id] 
 Essayez : 
 attend client.send_message ( 
 chat_id=f"@{admin_username}", 
"👋 Coucou, et bienvenue à toi dans *L’Enfer de Perséphone*, un espace d’échange où "
"_vulnérabilité rime avec force_, et où chaque présence compte.\n\n"
"Ici, on partage avec sincérité, douceur et respect.\n\n"
 Passe. 

print("LeCerbere_Bot est en ligne. Il veille sur ton sanctuaire.")
