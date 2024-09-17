
{
    'name': 'BMI Calculateur Snippet',
    "version": "16.0.1.0.1",
    'summary': 'Calculateur de IMC et Percentile',
    'description': """Ce bout de code ajoute une fonctionnalité à votre site web : un calculateur d'IMC et de percentiles pour enfants..""",
    'category': 'Website',
    'author': 'Adil',
    'website': 'http://www.votre-website.com',
    'depends': ['website'], # Assure-toi que le module 'website' est installé
    'data': [
        'views/assets.xml',
        'views/snippet_templates.xml',
        'views/snippet_Ajout_module.xml',
    ],
    'assets': {
        'web.assets_frontend': [
            # Utilisation des chemins complets pour CSS et JS
            'bmi_calculateur_snippet/static/src/css/snippet_style.css',
            'bmi_calculateur_snippet/static/src/js/bmi_calculator.js',
        ],
    },
 
    'installable': True,
    'auto_install': False,
    'license': 'AGPL-3',
}