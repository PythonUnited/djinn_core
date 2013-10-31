import pkg_resources
import os


def _class_implements(clazz, superclazz, check_self=True):

    well_does_it = False

    if check_self and clazz == superclazz:
        return True
    elif superclazz in  clazz.__bases__:
        well_does_it = True
    else:
        for base in clazz.__bases__:
            well_does_it = _class_implements(base, superclazz)
            if well_does_it:
                break

    return well_does_it


def implements(instance, clazz):

    """ Is it a bird? A plane? A clazz? """

    return _class_implements(instance.__class__, clazz)


def extends(clazz, otherclazz):

    """ Does the class extend the other one? """

    return _class_implements(clazz, otherclazz, check_self=False)


def find_locale_dirs():

    locale_dirs = []

    for entrypoint in pkg_resources.iter_entry_points(group="djinn.app"):

        locale_dir = os.path.join(entrypoint.dist.location, 
                                  entrypoint.module_name,
                                  'locale')

        if os.path.isdir(locale_dir):
            locale_dirs.append(locale_dir)

    return locale_dirs
