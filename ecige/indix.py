from nicegui import ui
import webbrowser
# WALID SALIMI
with ui.header():
    # contacte
    def open_gmail():
        email_address = "contact@ecig.ma"
        url = f"mailto:{email_address}"
        webbrowser.open(url)
    ui.button(icon='contact_support',color='bleu',on_click=lambda:open_gmail())
    # Localisation in map
    location = (34.26193723461011, -5.927029490551239)
    def open_map_at(location):
        url = f"https://www.google.com/maps/search/?api=1&query={location[0]},{location[1]}"
        webbrowser.open(url)
    ui.button(icon='pin_drop',color='bleu',on_click=lambda:open_map_at(location))

    ui.space()
    with ui.avatar():
        ui.image('ecig_image.png')
    ui.space()
with ui.row().style('width:100%'):
    with ui.column().style('width:44%'):
        ui.image('https://img.freepik.com/vecteurs-libre/www-concept-illustration_114360-2143.jpg').style('width:100%;highte:100%')
    with ui.column():
        ui.space()
        # Information Name
        name=ui.input(placeholder='Name').props('rounded outlined dense')
        Prename=ui.input(placeholder='Préname').props('rounded outlined dense')
        # Liste
        global options_pronch
        options_formation = ["Master et Licence","Technicien Spécialisé", "Technicien", "Qualification"]
        options_pronch = ["Devlopement informatique", "Géstion des Entreprises", "Gestion de Transport et Logistique"]
        def mix(e):

          field.clear()
          with field:
            options_formation = ["Master et Licence","Technicien Spécialisé", "Technicien", "Qualification"]
            select_formation = ui.select(options_formation,value=e.value,on_change=lambda e: mix(e)).classes('w-64')
            if e.value == "Master et Licence":
                options_pronch=["information", "achat,logistique,transport", "Gestion,management","Génie appliqeé"]
                select_pronch = ui.select(options_pronch,value=options_pronch[0]).classes('w-64')
                select_pronch.update()
            elif e.value == "Technicien Spécialisé":
                options_pronch = ["Devlopement informatique", "Géstion des Entreprises", "Gestion de Transport et Logistique"]
                select_pronch = ui.select(options_pronch,value=options_pronch[0]).classes('w-64')
                select_pronch.update()
            elif e.value == "Technicien":
                options_pronch = ["Gestion informatisée"]
                select_pronch = ui.select(options_pronch,value=options_pronch[0]).classes('w-64')
                select_pronch.update()
            else :
                options_pronch = ["Opérateur de Saisie"]
                select_pronch = ui.select(options_pronch,value=options_pronch[0]).classes('w-64')
                select_pronch.update()
        with ui.column().classes('w-full') as field:
             select_formation = ui.select(options_formation,value=options_formation[0],on_change=lambda e: mix(e)).classes('w-64')
             select_pronch = ui.select(options_pronch,value=options_pronch[0]).classes('w-64')
        num_clicks = 0
        # Multip element
        def card_dawnload():
            #  click button for dont spame
            global num_clicks
            num_clicks += 1
            if num_clicks >= 4:
                ui.disable('Dawnload')
            with ui.card().style('aligne-items:center;width:44;highte:30%')as card:
                with ui.row().style('width:100%'):
                    ui.label()
                    ui.space()
                    ui.button(icon='delete_forever',color='red',on_click=lambda: card.delete() )
                    ui.button(icon='download',color='green',on_click=lambda:())

        ui.button('telecharge', icon='download',color='green',on_click=lambda: card_dawnload())
ui.run()
