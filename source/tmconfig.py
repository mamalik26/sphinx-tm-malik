class DocumentInfos:

    title = u'Développement d’un site de vente de produits locaux entre agriculteurs et consommateurs.'
    first_name = 'Chebbi'
    last_name = 'Malik'
    author = f'{first_name} {last_name}'
    year = u'2023'
    month = u'Janvier'
    seminary_title = u'Développement Web'
    tutor = u"Cédric Donner"
    release = "(Version intermédiaire)"
    repository_url = "https://github.com/mamalik26/TM_Malik"

    @classmethod
    def date(cls):
        return cls.month + " " + cls.year

infos = DocumentInfos()