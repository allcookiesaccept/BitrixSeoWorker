rules = {
    'nb': {
        'monitory':{
            'top': {
            'brand': {'lineup': '', 'curved|brand': '', 'gaming|brand': '', 'brand|resolution': '', 'matrix|brand': '', 'brand|diagonal': ''},
            'brand|diagonal': {'curved|diagonal': 'brandless%diagonal', 'gaming|diagonal': 'brandless%diagonal',
                               'matrix|diagonal': 'brandless%diagonal', 'brand|diagonal': 'brandless%diagonal',},
            'brand|resolution': {'curved|resolution': 'brandless%resolution', 'gaming|resolution': 'brandless%resolution',
                                 'brand|resolution': 'brandless%resolution'},
            'curved': { 'curved|brand': '', 'curved|diagonal': '', 'curved|resolution': ''},
            'curved|brand': {'curved|brand': 'brandless%curved'},
            'curved|diagonal': {'brand|diagonal': 'diagonal', 'gaming|diagonal': 'diagonal', 'matrix|diagonal': 'diagonal'},
            'curved|hz': {'curved': '', 'hdr': '', 'height-adjustment': '', 'gaming': '', 'gaming|hz': 'hz', 'matrix|hz': 'hz'},
            'curved|resolution': {'brand|resolution': 'resolution', 'matrix|resolution': 'resolution', 'gaming|resolution': 'resolution'},
            'diagonal': {'brand|diagonal': 'diagonal', 'curved|diagonal': 'diagonal', 'gaming|diagonal': 'diagonal',
                         'matrix|diagonal': 'diagonal'},
            'gaming': {'curved': '', 'hdr': '', 'height-adjustment': '', 'gaming|brand': '', 'gaming|resolution': ''},
            'gaming|brand': {'gaming|brand': 'brandless%gaming'},
            'gaming|diagonal': {'brand|diagonal': 'diagonal', 'curved|diagonal': 'diagonal',
                                'matrix|diagonal': 'diagonal'},
            'gaming|hz': {'curved|hz': 'hz', 'matrix|hz': 'hz'},
            'gaming|resolution': {'brand|resolution': 'resolution', 'curved|resolution': 'resolution', 'matrix|resolution': 'resolution'},
            'hdr': {'height-adjustment': '', 'curved': '', 'gaming': '', 'resolution': ''},
            'height-adjustment': {'hdr': '', 'curved': '', 'gaming': '', 'resolution': ''},
            'lineup': {'lineup': ''},
            'matrix': {'matrix|brand': 'matrix', 'matrix|resolution': 'matrix'},
            'matrix|brand': {'matrix|brand': 'brandless%matrix'},
            'matrix|diagonal': {'matrix|diagonal': 'matrix', 'curved|diagonal': 'diagonal', 'gaming|diagonal': 'diagonal'},
            'matrix|hz': {'gaming|hz': 'hz', 'curved|hz': 'hz', 'matrix|resolution': 'matrix'},
            'matrix|resolution': {'brand|resolution': 'resolution', 'curved|resolution': 'resolution', 'gaming|resolution': 'resolution', 'matrix|resolution': 'resolution'},
            'resolution': {'brand|resolution': 'resolution', 'gaming|resolution': 'resolution', 'curved|resolution': 'resolution',
                           'matrix|resolution': 'resolution'},
    },
            'bottom': {
                'brand': {'brand': 'brandless', 'hdr': 'brandless', 'height-adjustment': 'brandless',
                          'curved': 'brandless', 'gaming': 'brandless'},
                'brand|diagonal': {'hdr': 'brandless', 'height-adjustment': 'brandless',
                          'curved': 'brandless', 'gaming': 'brandless', 'matrix': 'brandless', 'resolution': 'brandless'},
                'brand|resolution': {'hdr': 'brandless', 'height-adjustment': 'brandless',
                          'curved': 'brandless', 'gaming': 'brandless', 'brand': 'brandless',},
                'curved': {'curved|hz': '', 'hdr': 'brandless', 'height-adjustment': 'brandless',
                          'curved': 'brandless', 'gaming': 'brandless'},
                'curved|brand': {'gaming|brand': 'brand', 'matrix|brand': 'brand', 'brand|resolution': 'brand', 'brand': 'brandless'},
                'curved|diagonal': {'hdr': 'brandless', 'height-adjustment': 'brandless',
                          'curved': 'brandless', 'gaming': 'brandless', 'matrix': 'brandless', 'resolution': 'brandless'},
                'curved|hz': {'brand': '', 'hdr': '', 'height-adjustment': '', 'matrix': ''},
                'curved|resolution': {'brand': '', 'hdr': '', 'height-adjustment': '', 'matrix': ''},
                'diagonal': {'brand': '', 'hdr': '', 'height-adjustment': '', 'matrix': ''},
                'gaming': {'brand': '', 'hdr': '', 'height-adjustment': '', 'matrix': ''},
                'gaming|brand': {'matrix|brand': 'brand', 'brand|resolution': 'brand', 'curved|brand': 'brand'},
                'gaming|diagonal': {'brand': '', 'hdr': '', 'height-adjustment': '', 'matrix': ''},
                'gaming|hz': {'brand': '', 'hdr': '', 'height-adjustment': '', 'matrix': ''},
                'gaming|resolution': {'brand': '', 'hdr': '', 'height-adjustment': '', 'matrix': ''},
                'hdr': {'brand': '', 'hdr': '', 'height-adjustment': '', 'matrix': ''},
                'height-adjustment': {'brand': '', 'hdr': '', 'height-adjustment': '', 'matrix': ''},
                'lineup': {'brand': 'brandless', 'hdr': 'brandless', 'height-adjustment': 'brandless', 'matrix': 'brandless'},
                'matrix': {'brand': '', 'hdr': '', 'height-adjustment': '', 'matrix': ''},
                'matrix|brand': {'curved|brand': 'brand', 'gaming|brand': 'brand', 'brand|diagonal': 'brand'},
                'matrix|diagonal': {'matrix|brand': 'matrix'},
                'matrix|hz': {'brand': '', 'hdr': '', 'height-adjustment': '', 'matrix': ''},
                'matrix|resolution': {'brand': '', 'hdr': '', 'height-adjustment': '', 'matrix': ''},
                'resolution': {'brand': '', 'hdr': '', 'height-adjustment': '', 'matrix': ''},

            }

        },
        'notebooks': {
            'top': {
                'brand': {'series': '', 'brand|diagonal': '', 'brand|ultrabook': '', 'brand|transformery': ''},
                'brand|color': {'series|color': 'color'},
                'brand|diagonal': {'series|diagonal': 'diagonal'},
                'brand|transformery': {'brand|ultrabook': '', 'brand|color': ''},
                'brand|ultrabook': {'brand|transformery': '', 'series|ultrabook': ''},
                'brand|videocard': {'brand|videocard': 'videocard', 'series': ''},
                'color': {'brand|color': 'color'},
                'cpu_series': {'cpu_series': ''},
                'diagonal': {'brand|diagonal': 'diagonal'},
                'disk_configuration': {'ssd_capacity': '', 'disk_configuration': ''},
                'lineup':  {'series': 'find%series'},
                'matrix': {'matrix_surface': '', 'matrix|diagonal': 'matrix'},
                'matrix_surface': {'matrix_surface': ''},
                'matrix|diagonal': {'matrix|diagonal': 'matrix'},
                'series': {'lineup': 'find%lineup'},
                'series|color': {'series|color': 'color', 'series|diagonal': 'series', 'series|ultrabook': 'series'},
                'series|diagonal': {'series|color': 'series', 'series|diagonal': 'diagonal', 'series|ultrabook': 'series'},
                'series|ultrabook': {'series|color': 'series', 'series|diagonal': 'series', 'series|ultrabook': 'ultrabook'},
                'ssd_capacity': {'ssd_capacity': '', 'disk_configuration': ''},
                'transformery': {'brand|transformery': ''},
                'ultrabook': {'brand|ultrabook': ''},
                'videocard': {'brand|videocard': 'videocard'}
        },
        'bottom': {
            'brand': {'brand|color': '', 'brand|videocard': ''},
            'brand|color': {'brand|color': 'brandless%color'},
            'brand|diagonal': {'brand|diagonal': 'brandless%diagonal'},
            'brand|transformery': {'brand|transformery': 'brandless%transformery'},
            'brand|ultrabook': {'brand|ultrabook': 'brandless%ultrabook'},
            'brand|videocard': {'brand|videocard': 'brandless%videocard'},
            'color': {'brand|transformery': '', 'brand|ultrabook': ''},
            'cpu_series': {'videocard': ''},
            'diagonal': {'matrix': ''},
            'disk_configuration': {'cpu_series': ''},
            'lineup': {'series': ''},
            'matrix': {'matrix': '', 'diagonal': ''},
            'matrix_surface': {'matrix|diagonal': ''},
            'matrix|diagonal': {'matrix|diagonal': 'diagonal'},
            'series': {'brand|color': ''},
            'series|color': {'series|color': 'brandless%color'},
            'series|diagonal': {'series|diagonal': 'brandless%diagonal'},
            'series|ultrabook': {'series|ultrabook': 'brandless%ultrabook'},
            'ssd_capacity': {'videocard': ''},
            'transformery': {'brand': ''},
            'ultrabook': {'brand': ''},
            'videocard': {'cpu_series': ''}

        }


    },
        'pc': {
        'top': {
            'brand': {'gaming|brand': '', 'pc|brand': '', 'monoblock|brand': '', 'nettop|brand': '', 'series': ''},
            'gaming|brand': {'gaming|brand': 'brandless%gaming'},
            'gaming': {'gaming|brand': ''},
            'lineup': {'lineup': ''},
            'monoblock': {'monoblock|brand': ''},
            'monoblock|brand': {'monoblock|brand|diagonal': 'brand'},
            'monoblock|brand|diagonal': {'monoblock|brand|diagonal': 'brandless%diagonal'},
            'monoblock|diagonal': {'monoblock|brand|diagonal': 'diagonal'},
            'nettop': {'nettop|brand': ''},
            'nettop|brand': {'nettop|brand': 'brandless%nettop'},
            'pc': {'pc|brand': ''},
            'pc|brand': {'pc|brand': 'brandless%pc'},
            'series': {'lineup': ''}
        },

        'bottom': {
            'brand': {'lineup': ''},
            'gaming|brand': {'brand': ''},
            'gaming': {'brand': ''},
            'lineup': {'series': ''},
            'monoblock': {'monoblock|diagonal': ''},
            'monoblock|brand': {'monoblock|brand': 'brandless%monoblock'},
            'monoblock|brand|diagonal': {'monoblock|brand': 'brandless%monoblock'},
            'monoblock|diagonal': {'monoblock|brand': ''},
            'nettop': {'gaming|brand': ''},
            'nettop|brand': {'brand': ''},
            'pc': {'gaming|brand': ''},
            'pc|brand': {'brand': 'brandless', 'memory': 'brandless', 'color': 'brandless'},
            'series': {'brand': ''},

        }
           },
        'smartfony': {
        'top': {
            'brand': {'brand|memory': '', 'series': '', 'brand|color': ''},
            'diagonal': {'diagonal': ''},
            'memory': {'brand|memory': 'memory'},
            'color': {'brand|color': 'color'},
            'series': {'lineup': ''},
            'lineup': {'lineup': ''},
            'brand|color': {'brand|color': 'brandless%color'},
            'brand|memory': {'brand|memory': 'brandless%memory'},
        },
        'bottom': {
            'brand': {'brand': 'brandless', 'memory': 'brandless', 'color': 'brandless'},
            'diagonal': {'brand': ''},
            'memory': {'memory': ''},
            'color': {'color': ''},
            'series': {'brand': 'brandless', 'memory': 'brandless', 'color': 'brandless'},
            'lineup': {'brand': 'brandless', 'memory': 'brandless', 'color': 'brandless'},
            'brand|color': {'color': 'brandless'},
            'brand|memory': {'memory': 'brandless'},
        }
    },
        'planshety': {
        'top':  {
            'brand': {'series': '', 'lineup': '', 'brand|diagonal': ''},
            'memory': {'lineup|memory': 'brandless%memory'},
            'diagonal': {'brand|diagonal': 'brandless%diagonal'},
            'color': {'lineup|color': 'brandless%color'},
            'series': {'lineup': ''},
            'lineup': {'lineup|color': 'lineup', 'lineup|memory': 'lineup'},
            'lineup|color': {'lineup': ''},
            'lineup|memory': {'lineup': ''},
            'brand|diagonal': {'brand|diagonal': 'brandless%diagonal'},
                               },
        'bottom': {
            'brand': {'brand': 'brandless', 'memory': 'brandless', 'color': 'brandless'},
            'memory': {'brand': 'brandless', 'memory': 'brandless', 'color': 'brandless'},
            'diagonal': {'brand': 'brandless', 'memory': 'brandless', 'color': 'brandless'},
            'color': {'brand': 'brandless', 'memory': 'brandless', 'color': 'brandless'},
            'series': {'brand': 'brandless', 'memory': 'brandless', 'color': 'brandless'},
            'lineup': {'brand': 'brandless', 'memory': 'brandless', 'color': 'brandless'},
            'lineup|color': {'brand': 'brandless', 'memory': 'brandless', 'color': 'brandless'},
            'lineup|memory': {'brand': 'brandless', 'memory': 'brandless', 'color': 'brandless'},
            'brand|diagonal': {'brand': 'brandless', 'memory': 'brandless', 'color': 'brandless'},
            }
        
        
        
    }
        },
    'iport': {
        'ipad': {
            'top': {
                'color': {'lineup|color': 'color'},
                'lineup': {'lineup|color': 'lineup', 'lineup|diagonal': 'lineup', 'lineup|memory': 'lineup', 'lineup|year': 'lineup'},
                'lineup|color': {'lineup|color': 'lineup', 'lineup|diagonal': 'lineup', 'lineup|memory': 'lineup', 'lineup|year': 'lineup'},
                'lineup|diagonal': {'lineup|color': 'lineup', 'lineup|diagonal': 'lineup', 'lineup|memory': 'lineup', 'lineup|year': 'lineup'},
                'lineup|memory': {'lineup|color': 'lineup', 'lineup|diagonal': 'lineup', 'lineup|memory': 'lineup', 'lineup|year': 'lineup'},
                'lineup|year': {'lineup|color': 'lineup', 'lineup|diagonal': 'lineup', 'lineup|memory': 'lineup', 'lineup|year': 'lineup'},
                'memory': {'lineup|memory': 'memory'},
                'year': {'lineup|year': 'year'},
                    },
            'bottom': {
                'color': {'lineup': '', 'memory': '', 'year': ''},
                'lineup': {'lineup': '', 'memory': '', 'year': ''},
                'lineup|color': {'lineup|color': 'color', 'lineup': '', 'memory': '', 'year': ''},
                'lineup|diagonal': {'lineup': '', 'memory': '', 'year': ''},
                'lineup|memory': {'lineup|memory': 'memory', 'lineup': '', 'memory': '', 'year': ''},
                'lineup|year': {'lineup|year': 'year', 'lineup': '', 'memory': '', 'year': ''},
                'memory': {'lineup': '', 'memory': '', 'year': ''},
                'year': {'lineup': '', 'memory': '', 'year': ''},
            }


    }

    }
}



