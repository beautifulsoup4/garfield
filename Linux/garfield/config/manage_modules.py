from garfield.config.soft_import_module import soft_import
from garfield.softwares.browsers.firefox_browsers import firefox_browsers
from garfield.softwares.browsers.chromium_browsers import chromium_browsers

try:
    from garfield.softwares.memory.memorydump import MemoryDump
except ImportError:
    pass


def get_categories():
    category = {
        'chats': {'help': 'Chat clients supported'},
        'sysadmin': {'help': 'SCP/SSH/FTP/FTPS clients supported'},
        'databases': {'help': 'SQL clients supported'},
        'mails': {'help': 'Email clients supported'},
        'memory': {'help': 'Retrieve passwords from memory'},
        'wifi': {'help': 'Wifi'},
        'browsers': {'help': 'Web browsers supported'},
        'wallet': {'help': 'Windows credentials (credential manager, etc.)'},
        'git': {'help': 'GIT clients supported'},
        'unused': {'help': 'This modules could not be used because of broken dependence'}
    }
    return category


def get_modules_names():
    return [
        ("garfield.softwares.mails.clawsmail", "ClawsMail"),
        ("garfield.softwares.mails.thunderbird", "Thunderbird"),
        ("garfield.softwares.databases.dbvis", "DbVisualizer"),
        ("garfield.softwares.sysadmin.env_variable", "Env_variable"),
        ("garfield.softwares.sysadmin.apachedirectorystudio", "ApacheDirectoryStudio"),
        ("garfield.softwares.sysadmin.filezilla", "Filezilla"),
        ("garfield.softwares.sysadmin.fstab", "Fstab"),
        ("garfield.softwares.browsers.opera", "Opera"),
        ("garfield.softwares.chats.pidgin", "Pidgin"),
        ("garfield.softwares.chats.psi", "PSI"),
        ("garfield.softwares.sysadmin.shadow", "Shadow"),
        ("garfield.softwares.sysadmin.aws", "Aws"),
        ("garfield.softwares.sysadmin.docker", "Docker"),
        ("garfield.softwares.sysadmin.rclone", "Rclone"),
        ("garfield.softwares.sysadmin.ssh", "Ssh"),
        ("garfield.softwares.sysadmin.cli", "Cli"),
        ("garfield.softwares.sysadmin.gftp", "gFTP"),
        ("garfield.softwares.sysadmin.keepassconfig", "KeePassConfig"),
        ("garfield.softwares.sysadmin.grub", "Grub"),
        ("garfield.softwares.databases.sqldeveloper", "SQLDeveloper"),
        ("garfield.softwares.databases.squirrel", "Squirrel"),
        ("garfield.softwares.wifi.wifi", "Wifi"),
        ("garfield.softwares.wifi.wpa_supplicant", "Wpa_supplicant"),
        ("garfield.softwares.wallet.kde", "Kde"),
        ("garfield.softwares.wallet.libsecret", "Libsecret"),
        ("garfield.softwares.memory.mimipy", "Mimipy"),
        ("garfield.softwares.git.gitforlinux", "GitForLinux")
    ]

    # very long to execute
    # try:
    # 	module_names.append(MemoryDump())
    # except:
    # 	pass


def get_modules():
    modules = [soft_import(package_name, module_name)() for package_name, module_name in get_modules_names()]
    return modules + chromium_browsers + firefox_browsers
