# Klipper printers

*0.8.6 pre-release* · Spoolman, or BamBuddy that keeps its spools in Spoolman

The original's AMS view shows the Bambu printers of FilaMan or BamBuddy (see the [original's documentation](https://niko11111.github.io/SpoolmanScale-Docs/use/ams/)). This fork adds Klipper printers to it: a weighed spool goes into a gate, lane or tool of a Klipper printer, through Moonraker. BamBuddy learns nothing about these printers.

## What the printer needs

- **Moonraker with a `[spoolman]` section** that points to the **same Spoolman** as the scale.
- **Moonraker must trust the scale:** add the scale's address under `trusted_clients` in Moonraker, or enter a Moonraker API key on the scale.

## Adding a printer

**Web interface → Klipper → Add printer:** a name, the address (IP or host name), the port (7125 unless you changed it) and, only if Moonraker does not trust the scale, an API key. Up to 64 printers. The name is at most 23 characters (umlauts and accents count double) and becomes the location of the spools in that printer.

After every save, and with **Test connection**, the scale checks the printer. The test only reads. It reports, in this order:

| Step | When it fails |
|---|---|
| Moonraker answers | Not reachable - check address and port |
| Access is allowed | Access denied - add the scale's address in Moonraker as trusted (trusted_clients) or enter an API key |
| Klipper is ready | Klipper not ready |
| Spoolman is set up in Moonraker | Spoolman is not set up in Moonraker ([spoolman]) |
| Moonraker is connected to it | Spoolman set up, but not connected |
| It is the scale's Spoolman | Another Spoolman than the scale's - assigning blocked |

When everything passes: "Connected: <what the printer has>, Spoolman connected, same Spoolman". Assigning to a printer only works after a test that passed.

## What the scale detects

Nothing to choose by hand. The test finds out what the printer has:

- a **Happy Hare** MMU with its gates;
- an **AFC** unit (Box Turtle and others) with its lanes;
- **tool macros** `T0`, `T1`, … with a `spool_id` variable, the convention of Mainsail and Fluidd for toolchangers;
- otherwise one field for Moonraker's **active spool**.

## In the AMS view

The printer button at the top of the AMS view shows the printer's name with an arrow. A tap opens **Choose printer**: every printer as a button in two columns, with its name and what it is (the Bambu model, or "Klipper" with its tools, MMU slots or AFC slots); the current one has a tick. A magnifier searches names and kinds: "jar" finds Jarvis, "klipper" every Klipper printer. **Cancel** or back leaves everything as it was. This works on all three boards and for Bambu printers too.

A Klipper printer shows its gates, lanes or tools in groups of four, with the spool each one holds: colour and material from the printer or from Spoolman, the grams from Spoolman.

**Assigning:** weigh a spool, then **into which bay?** → the Klipper printer → the field. Or **More info → Into AMS**. The printer then holds the spool there (as Mainsail or Fluidd show), and the spool's location in Spoolman becomes the printer's name. Happy Hare in `push` or `pull` mode sets the location itself.

## The displaced spool gets its old location back

When the scale assigns a spool to a Klipper printer, it remembers the spool's previous location in Spoolman, in an extra field **Location before the printer** that the scale creates once. When a later assignment puts another spool into the same field, the displaced spool gets its old location back, if its location is still the printer's name. Without a remembered location, its location is cleared.

Not for Happy Hare in `push`/`pull`. A spool swapped at the printer itself, in Mainsail for example, goes unnoticed by the scale. With BamBuddy, this goes to Spoolman directly, because BamBuddy does not pass extra fields on.
