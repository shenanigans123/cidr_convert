# CIDR Convert
Plugin for Sublime Text Editor 2/3

Converts IPv4 addresses to/from cidr notation. Detects and converts addresses between the formats:

- 192.168.1.0 255.255.255.0
- 192.168.1.0/24

Acts on entire document if no text is selected, otherwise only acts within selected area.

# Usage
Adds menu entries:
```
Edit -> Text -> CIDR On
             -> CIDR Off
```

Default keyboard shortcuts:

Windows/Linux:
- `Ctrl+Alt+/ -> CIDR On`
- `Ctrl+Alt+. -> CIDR Off`

Mac:
- `Ctrl+⌘+/ -> CIDR On`
- `Ctrl+⌘+. -> CIDR Off`
