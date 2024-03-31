from nicegui import ui
import webbrowser
from firebase_admin import storage
import os
with ui.header():
    def open_gmail():
        email_address = "contact@ecig.ma"
        url = f"mailto:{email_address}"
        webbrowser.open(url)
    ui.button(icon='contact_support',color='bleu',on_click=lambda:open_gmail())

    location = (34.26193723461011, -5.927029490551239)
    def open_map_at(location):
        url = f"https://www.google.com/maps/search/?api=1&query={location[0]},{location[1]}"
        webbrowser.open(url)
    ui.button(icon='pin_drop',color='bleu',on_click=lambda:open_map_at(location))

    ui.space()
    with ui.avatar():
        ui.image('data:image/png;base64,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')
    ui.space()
    ui.label()
with ui.row().style('width:100%'):
    with ui.column().style('width:44%'):
        ui.image('https://img.freepik.com/vecteurs-libre/www-concept-illustration_114360-2143.jpg').style('width:100%;highte:100%')
    with ui.column():
        ui.space()
        name=ui.input(placeholder='Name').props('rounded outlined dense')
        Prename=ui.input(placeholder='Préname').props('rounded outlined dense')
        options_formation = ["Master et Licence","Technicien Spécialiś", "Technicien", "Qualification"]
        options_pronch = ["Devlopement informatique", "Géstion des Entreprises", "Gestion de Transport et Logistique"]
        select_formation = ui.select(options_formation,label='Formation').classes('w-64')
        if options_formation== [0]:
            options_pronch.clear()
            options_pronch=["information", "achat,logistique,transport", "Gestion,management","Génie appliqeé"]
            print("ffff")
        elif options_formation== "Technicien Spécialiś":
            pass
        elif options_formation== "Technicien":
            options_pronch.clear()
            options_pronch.extend(["Gestion informatisée"])
        else:
            options_pronch.clear()
            options_pronch.extend(["Opérateur de Saisie"])
        select_pronch = ui.select(options_pronch).classes('w-64')
        #fairbase for instalation fille

        def download_file():
            storage_client = storage.initialize_app().storage()
            file_path = "gs://data-bas-84e8f.appspot.com/exam.png"
            local_file_path = "downloaded_file.txt"
            blob = storage_client.bucket().get_blob(file_path)
            blob.download_to_filename(local_file_path)
            os.startfile(local_file_path)

        def card_dawnload():
                with ui.card().style('aligne-items:center;width:44;highte:30%')as card:
                    with ui.row().style('width:100%'):
                        ui.label()
                        ui.space()
                        ui.button(icon='delete_forever',color='red',on_click=lambda: card.clear() )
                        ui.button(icon='download',color='green',on_click=lambda:download_file())
                        download_file()
        ui.button('telecharge', icon='download',color='green',on_click=lambda: card_dawnload())


ui.run()