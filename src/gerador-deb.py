from imports import *
from Tools import *


def START():
    App.focus()
    
    VALIDATION = Validation(
        Package     = EntryName.get().replace(" ", "-").lower().strip(),
        Maintainer  = EntryMaintainer.get().strip(),
        Version     = EntryVersion.get().lower().strip(),
        Description = EntryDescription.get().strip(),
        Icon        = EntryIcon.get(),
        Exec        = EntryExec.get(),
    )
    
    IsOk = False
    if (VALIDATION[0][0] and VALIDATION[1][0] and 
        VALIDATION[2][0] and VALIDATION[3][0] and 
        VALIDATION[4][0] and VALIDATION[5][0] ):
        IsOk = True

    # Package 
    if VALIDATION[0][0] == False:
        EntryName.configure(
            placeholder_text       = f"{VALIDATION[0][1]}",
            border_width           = 2,
            border_color           = "#740C0C",
            placeholder_text_color = "#740C0C",
        )
        EntryName.delete(0, "end")
        EntryName.focus_force()
    else:EntryName.configure(
            border_width     = 2,
            border_color     = "#09862F",
        )


    # Maintainer
    if VALIDATION[1][0] == False:
        EntryMaintainer.configure(
            placeholder_text       = f"{VALIDATION[1][1]}",
            border_width           = 2,
            border_color           = "#740C0C",
            placeholder_text_color = "#740C0C",
        )
        EntryMaintainer.delete(0, "end")
        EntryMaintainer.focus_force()
    else:EntryMaintainer.configure(
            border_width = 2,
            border_color = "#09862F",
        )
    

    # Version
    if VALIDATION[2][0] == False:
        EntryVersion.configure(
            placeholder_text       = f"{VALIDATION[2][1]}",
            border_width           = 2,
            border_color           = "#740C0C",
            placeholder_text_color = "#740C0C",
        )
        EntryVersion.delete(0, "end")
        EntryVersion.focus_force()
    else:EntryVersion.configure(
            border_width = 2,
            border_color = "#09862F",
        )


    styleErro = ttk.Style()
    styleErro.theme_use('clam')
    styleErro.configure(
        "Erro_CustomCombobox.TCombobox",
        bordercolor = "#740C0C",
        font        = ("Consolas", 14)
        )

    styleOk = ttk.Style()
    styleOk.theme_use('clam')
    styleOk.configure(
        "OK_CustomCombobox.TCombobox",
        bordercolor = "#09862F",
        font        = ("Consolas", 14)
    )


    # Description
    if VALIDATION[3][0] == False:
        EntryDescription.configure(
            placeholder_text       = f"{VALIDATION[3][1]}",
            border_width           = 2,
            border_color           = "#740C0C",
            placeholder_text_color = "#740C0C",
        )
        EntryDescription.delete(0, "end")
        EntryDescription.focus_force()
    else:EntryDescription.configure(
            border_width = 2,
            border_color = "#09862F",
        )

    App.focus()

    # Icon
    EntryIcon.configure(state="normal")
    if (VALIDATION[4][0] == False):
        EntryIcon.configure(
            border_width  = 2,
            border_color  = "#740C0C",
            text_color    = "#740C0C"
        )
        EntryIcon.delete(0, "end")
        EntryIcon.insert(0, VALIDATION[4][1])
    else:EntryIcon.configure(
            border_width = 2,
            border_color = "#09862F",
            text_color   = "#000000"
        )
    EntryIcon.configure(state="readonly")
    
    
    # Exec
    EntryExec.configure(state="normal")
    if VALIDATION[5][0] == False:
        EntryExec.configure(
            border_width = 2,
            border_color = "#740C0C",
            text_color   = "#740C0C"
        )
        EntryExec.delete(0, "end")
        EntryExec.insert(0, VALIDATION[5][1])
    else:EntryExec.configure(
            border_width = 2,
            border_color = "#09862F",
            text_color   = "#000000"
        )
    EntryExec.configure(state="readonly")

    if IsOk == False:
        TxStatus.configure(
            text        = "─ ERROR: FILE NOT CREATED! ─",
            text_color  = "#740C0C"
        )
    else:
        DIR = SelectLocaleDir("Select where to save your .deb package")
        if DIR:
            TxStatus.configure(
                text       = "─ OK: CREATING FILES! ─",
                text_color = "#EBE712"
            )
            CreatePATH(
                DIR          = DIR,
                AppName      = EntryName.get().strip(),
                Version      = EntryVersion.get().lower().strip(),
                Section      = EntrySection.get().strip(),
                Priority     = EntryPriority.get().strip(),
                Architecture = EntryArchitecture.get().strip(),
                Categories   = EntryCategories.get().strip(),
                Terminal     = EntryTerminal.get(),
                Maintainer   = EntryMaintainer.get().strip(),
                Description  = EntryDescription.get().strip(),
                DirIcon      = EntryIcon.get(),
                DirExec      = EntryExec.get(),
            )
            TxStatus.configure(
                text       = "─ OK: FILES CREATED SUCCESSFULLY! ─",
                text_color = "#09862F"
            )
        else:
            TxStatus.configure(
                text        = "─ ERROR: NO DIRECTORY FOR FILES! ─",
                text_color  = "#740C0C"
            )



# Inint code:
CTK.set_appearance_mode("light")
CTK.set_default_color_theme("green")

App = CTK.CTk()
App.title("Gerador DEB")
App.geometry("700x600")
App.resizable(False, False)

FONT = CTK.CTkFont(size=16, weight="bold", family="Consolas")


Container = CTK.CTkFrame(
    master        = App,
    fg_color      = "transparent",
    border_width  = 0,
    corner_radius = 15,
);Container.pack(pady=10, padx=10, fill="both", expand=True)

Line(Container)

# line > Titule
LineTitule = CTK.CTkFrame(
    master   = Container,
    fg_color = "transparent"
);LineTitule.pack(pady=(3, 0), anchor="w", fill="x")
Titule = CTK.CTkLabel(
    master = LineTitule,
    text   = " - Package Informations - ",
    font   = CTK.CTkFont(size=20, weight="bold"),
);Titule.pack()

# Line > App Name
LineName = CTK.CTkFrame(
    master   = Container,
    fg_color = "transparent"
);LineName.pack(padx=(10, 5), pady=(15, 0), anchor="w", fill="x")
TxName = CTK.CTkLabel(
    master = LineName,
    text   = "App Name ─────",
    font   = FONT,
);TxName.pack(side="left")
EntryName = CTK.CTkEntry(
    master           = LineName,
    width            = 700,
    placeholder_text = "Your app name",
    border_width     = 0,
);EntryName.pack(side="left", padx=(10, 0))

# Line > Maintainer
LineMaintainer = CTK.CTkFrame(
    master   = Container,
    fg_color = "transparent"
);LineMaintainer.pack(padx=(10, 5), pady=(5, 0), anchor="w", fill="x")
TxMaintainer = CTK.CTkLabel(
    master = LineMaintainer,
    text   = "Maintainer ───",
    font   = FONT
);TxMaintainer.pack(side="left")
EntryMaintainer = CTK.CTkEntry(
    master           = LineMaintainer,
    placeholder_text = "Your: First_name Last_name <email@dominio.com>",
    width            = 700,
    border_width     = 0
);EntryMaintainer.pack(side="left", padx=(10, 0))

# Line > Version
LineVersion = CTK.CTkFrame(
    master   = Container,
    fg_color = "transparent"
);LineVersion.pack(padx=(10, 5), pady=(5, 0), anchor="w", fill="x")
TxVersion = CTK.CTkLabel(
    master = LineVersion,
    text   = "Version ──────",
    font   = FONT
);TxVersion.pack(side="left")
EntryVersion = CTK.CTkEntry(
    master           = LineVersion,
    width            = 700,
    placeholder_text = "Your app version",
    border_width     = 0
);EntryVersion.pack(side="left", padx=(10, 0))

style = ttk.Style()
style.theme_use('clam')
style.configure(
    "CustomCombobox.TCombobox",
    bordercolor="#CCCCCC",
    font=("Consolas", 14)
)

# Line > Section
LineSection = CTK.CTkFrame(
    master   = Container,
    fg_color = "transparent"
);LineSection.pack(padx=(10, 5), pady=(5, 0), anchor="w", fill="x")
TxSection = CTK.CTkLabel(
    master = LineSection,
    text   = "Section ──────",
    font   = FONT
);TxSection.pack(side="left")
SECTION_OPTIONS = [
    "utils", "admin", "cli-mono", "comm", "database", "debug", 
    "devel", "doc", "editors", "education", "electronics", "embed", 
    "fonts", "games", "gnome", "graphics", "hamradio", "interpreters", 
    "kde", "libdevel", "libs", "mail", "math", "metapackages", "misc", 
    "net", "news", "oldlibs", "otherosfs", "patches", "perl", "php", 
    "python", "ruby", "science", "shells", "sound", "tasks", "tex", 
    "text", "vcs", "video", "web", "x11",
]
EntrySection = ttk.Combobox(
    master = LineSection,
    width  = 25,
    values = SECTION_OPTIONS,
    style  = "CustomCombobox.TCombobox"
);EntrySection.pack(side="left", padx=(10, 0))
EntrySection.set("utils")
EntrySection.configure(state="readonly")

# Line > Categories
LineCategories = CTK.CTkFrame(
    master   = Container,
    fg_color = "transparent"
);LineCategories.pack(padx=(10, 5), pady=(5, 0), anchor="w", fill="x")
TxCategories = CTK.CTkLabel(
    master = LineCategories,
    text   = "Categories ───",
    font   = FONT
);TxCategories.pack(side="left")
CATEGORIES_OPTIONS = [
    "Utility", "Development", "IDE", "GUIDesigner", "Building", "Debugger", "Profiling", "System",
    "FileTools", "Archiving", "TerminalEmulator", "TextEditor", "Network", "WebBrowser", "Email", "Chat",
    "InstantMessaging", "VideoConference", "News", "Graphics", "2DGraphics", "3DGraphics", "VectorGraphics",
    "RasterGraphics", "Photography", "Scanning", "AudioVideo", "Audio", "Video", "Player", "Recorder", "TV",
    "Mixer", "Game", "ActionGame", "AdventureGame", "ArcadeGame", "BoardGame", "CardGame", "RolePlaying",
    "Simulation", "SportsGame", "StrategyGame", "Education", "Science", "Math", "Languages", "Engineering",
    "Astronomy", "Chemistry", "Physics", "Settings", "PackageManager", "Security", "Printing", "Monitor",
    "HardwareSettings"
]
EntryCategories = ttk.Combobox(
    master = LineCategories,
    width  = 25,
    values = CATEGORIES_OPTIONS,
    style  = "CustomCombobox.TCombobox"
);EntryCategories.pack(side="left", padx=(10, 0))
EntryCategories.set("Development")
EntryCategories.configure(state="readonly")

# Line > Architecture
LineArchitecture = CTK.CTkFrame(
    master   = Container,
    fg_color = "transparent"
);LineArchitecture.pack(padx=(10, 5), pady=(5, 0), anchor="w", fill="x")
TxArchitecture = CTK.CTkLabel(
    master = LineArchitecture,
    text   = "Architecture ─",
    font   = FONT
);TxArchitecture.pack(side="left")
EntryArchitecture = CTK.CTkSegmentedButton(
    master       = LineArchitecture,
    values       = ["amd64","i386","arm64","armhf","armel","ppc64el","s390x","mips","mipsel","all"],
    border_width = 0,
    font         = CTK.CTkFont(size=13, weight="bold"),
);EntryArchitecture.pack(side="left", padx=(10, 0))
EntryArchitecture.set("amd64")

# Line > Priority
LinePriority = CTK.CTkFrame(
    master   = Container,
    fg_color = "transparent"
);LinePriority.pack(padx=(10, 5), pady=(5, 0), anchor="w", fill="x")
TxPriority = CTK.CTkLabel(
    master = LinePriority,
    text   = "Priority ─────",
    font   = FONT,
);TxPriority.pack(side="left")
EntryPriority = CTK.CTkSegmentedButton(
    master       = LinePriority,
    values       = ["optional", "standard", "extra", "required", "important"],
    border_width = 0,
    font         = CTK.CTkFont(size=13 ,weight="bold"),
);EntryPriority.pack(side="left", padx=(10, 0))
EntryPriority.set("optional")

# Line > Terminal
LineTerminal = CTK.CTkFrame(
    master   = Container,
    fg_color = "transparent"
);LineTerminal.pack(padx=(10, 5), pady=(5, 0), anchor="w", fill="x")
TxTerminal = CTK.CTkLabel(
    master = LineTerminal,
    text   = "Terminal ─────",
    font   = FONT
);TxTerminal.pack(side="left")
EntryTerminal = CTK.CTkSegmentedButton(
    master       = LineTerminal,
    values       = ["True", "False"],
    border_width = 0,
    font         = CTK.CTkFont(size=13, weight="bold"),
);EntryTerminal.pack(side="left", padx=(10, 0))
EntryTerminal.set("True")

# Line > Icon 
LineIcon = CTK.CTkFrame(
    master   = Container,
    fg_color = "transparent"
);LineIcon.pack(padx=(10, 5), pady=(5, 0), anchor="w", fill="x")
TxIcon = CTK.CTkLabel(
    master = LineIcon,
    text   = "Icon ─────────",
    font   = FONT
);TxIcon.pack(side="left")
IconButton = CTK.CTkButton(
    master  = LineIcon,
    width   = 50,
    command = lambda: SelectFileDir(EntryIcon, "Select your app icon"),
    text    = "📂",
);IconButton.pack(side="left", padx=(10, 0), pady=(0, 0))
EntryIcon = CTK.CTkEntry(
    master           = LineIcon,
    placeholder_text = "Directory to your app icon (128x128)",
    width            = 700,
    border_width     = 0
);EntryIcon.pack(side="left", padx=(10, 0), pady=(0, 0))
EntryIcon.configure(state="readonly")

# Line > Exec
LineExec = CTK.CTkFrame(
    master   = Container,
    fg_color = "transparent"
);LineExec.pack(padx=(10, 5), pady=(5, 0), anchor="w", fill="x")
TxExec = CTK.CTkLabel(
    master = LineExec,
    text   = "Exec ─────────",
    font   = FONT
);TxExec.pack(side="left")
ExecButton = CTK.CTkButton(
    master  = LineExec,
    width   = 50,
    command = lambda: SelectFileDir(EntryExec, "Select your executable"),
    text    = "📂"
);ExecButton.pack(side="left", padx=(10, 0), pady=(0, 0))
EntryExec = CTK.CTkEntry(
    master           = LineExec,
    placeholder_text = "Diretory to your executable",
    width            = 700,
    border_width     = 0
);EntryExec.pack(side="left", padx=(10, 0), pady=(0, 0))
EntryExec.configure(state="readonly")

# Line > Description
LineDescription = CTK.CTkFrame(
    master   = Container,
    fg_color = "transparent"
);LineDescription.pack(padx=(10, 5), pady=(5, 0), anchor="w", fill="x")
TxDescription = CTK.CTkLabel(
    master = LineDescription,
    text   = "Description ──",
    font   = FONT
);TxDescription.pack(side="left")
EntryDescription = CTK.CTkEntry(
    master           = LineDescription,
    placeholder_text = "Your app description",
    width            = 700,
    border_width     = 0
);EntryDescription.pack(side="left", padx=(10, 0))

Line(Container, Y=(15, 0))

# Line > Status
LineStatus = CTK.CTkFrame(
    master   = Container,
    fg_color = "transparent"
);LineStatus.pack(padx=(10, 5), pady=(5, 0), fill="x")
TxStatus = CTK.CTkLabel(
    master = LineStatus,
    text   = "─ STATUS ─",
    font   = FONT
);TxStatus.pack(padx=(10, 0), pady=(0, 0))

Line(Container, Y=(0, 0))

# Button start
ButtonStart = CTK.CTkButton(
    master  = Container,
    text    = "Generate .DEB",
    font    = CTK.CTkFont(size=16, weight="bold"),
    command = START,
    width   = 150,
    height  = 50,
);ButtonStart.pack(pady=(20, 20))

Line(Container, Y=(0, 0))

App.mainloop()