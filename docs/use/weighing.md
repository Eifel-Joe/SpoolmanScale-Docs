# Weighing and empty spools

Weighing itself works as in the original (see the [original's documentation](https://niko11111.github.io/SpoolmanScale-Docs/use/weighing/)). This fork adds parts that come off every weight, empty spool weights and spool types with BamBuddy and Spoolman, and a question when a spool weighs more than its label says.

## Parts on the spool

*since 0.8.5* · every backend

An NFC tag in a clip that moves from spool to spool, a filament clip, a holder: their weight comes off on top of the empty spool, everywhere a filament weight is worked out from the reading, also when an empty spool is weighed.

- **Web interface → Settings → Parts on the spool:** up to 8 parts with name and weight. The ones ticked (up to 3) apply to every spool.
- **At the scale:** the chip at the top right of the weight window opens **Parts on this spool**. A choice made there belongs to that spool, and the scale remembers it.

## Empty spool weight and spool types

*since 0.8.5* · BamBuddy with Spoolman

BamBuddy keeps a catalog of empty spools (maker, name, weight). The scale offers them as **spool types** and stores the chosen weight as the spool's own empty weight in Spoolman. A spool without one inherits the empty weight of its filament or its maker, as Spoolman does.

**Weight window → Options → Empty spool weight** offers four ways:

| Choice | What happens |
|---|---|
| **Weigh the empty spool** | the empty spool on the scale now, without its parts |
| **Enter the empty weight** | a weight you know, or the maker's |
| **Pick a spool type from the list** | **Choose the spool type**: the maker's types first, **Show all** for every type, a magnifier to search, **Add new** for a type that is missing |
| **Weigh the full spool** | an unopened spool on the scale and its filament weight: the empty weight is the reading without parts minus the filament weight |

**First weighing of an unused spool:** if the spool has no fitting empty weight of its own, the scale suggests the spool type that fits the reading. **Take measured** keeps the measured empty weight, **Other type** opens the list, **Later** leaves the spool as it is. While it asks, automatic sending waits.

**A new spool type** from an empty spool: **Settings → Spools & scale → Add empty spool**. Put the empty spool on, tap the parts on it, **Next**, give it a name. It is added to BamBuddy's catalog.

Spools created at the scale ask for the type as well, see [Creating spools](spools.md).

## Raise the label

*since 0.8.5* · BamBuddy with Spoolman

Spoolman caps the remaining weight at the label (initial) weight. When a weighing comes out more than 2 g above the label, the scale asks first instead of losing the difference: **Raise label to <n> g** sets the label to the weighed filament, **Keep the label** stores the label weight. With BamBuddy's own inventory the original already asks the same.
