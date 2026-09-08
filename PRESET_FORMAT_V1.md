# SignalWorks Studio `.preset` format v1

A `.preset` file is UTF-8 JSON. It stores portable plotting and engineering-limit configuration. It does **not** contain CSV measurements or test-specific graph comments.

V4.4.0 extends format v1 with optional `reference_lines` and `range_bands`. Older preset files remain compatible because both fields are optional.

```json
{
  "format": "SignalWorksStudioPreset",
  "format_version": 1,
  "name": "My Project Preset",
  "tabs": [
    {
      "name": "Tab1",
      "title": "Overall Parameter",
      "x_label": "Time",
      "auto_title": false,
      "axes": {
        "primary": {"label": "Voltage (V)", "min": "0", "max": "1000", "step": "50"},
        "secondary": {"label": "Current (A)", "min": "-100", "max": "100", "step": "10"}
      },
      "signals": [
        {"name": "Vdc_Out", "axis": "left", "color": null},
        {"name": "Idc_Out", "axis": "right", "color": "#FF00FF"}
      ],
      "reference_lines": [
        {
          "id": "line_example",
          "label": "Upper Limit",
          "value": 410,
          "axis": "left",
          "color": "#D92D20",
          "width": 2.0,
          "dash": "dash",
          "show_label": true,
          "visible": true
        }
      ],
      "range_bands": [
        {
          "id": "band_example",
          "label": "Accept Range",
          "min": 390,
          "max": 410,
          "axis": "left",
          "line_color": "#12B76A",
          "fill_color": "#12B76A",
          "opacity": 0.10,
          "width": 1.2,
          "dash": "dash",
          "show_label": true,
          "visible": true
        }
      ]
    }
  ]
}
```

## Signal fields

- `name`: exact CSV numeric column/header name.
- `axis`: `left` for Primary or `right` for Secondary.
- `color`: `null` uses the automatic palette. `#RRGGBB` forces a manual color.

## Reference line fields

- `label`: human-readable limit/requirement name.
- `value`: Y-axis value.
- `axis`: `left` / `right`.
- `color`: `#RRGGBB`.
- `width`: line width in pixels/points.
- `dash`: `solid`, `dash`, `dot`, `dashdot`, or `longdash`.
- `show_label`: show the line label on the graph.
- `visible`: initial visibility.

## Range band fields

- `label`: band name.
- `min`, `max`: lower and upper Y limits.
- `axis`: `left` / `right`.
- `line_color`: boundary color.
- `fill_color`: shaded-region color.
- `opacity`: 0.0–0.8 recommended.
- `width`, `dash`, `show_label`, `visible`: same concept as Reference Lines.

## Comments

Graph comments are intentionally **not** part of `.preset` v1 export. Comments describe a specific test log/event, while presets are intended to describe reusable plotting and requirement configuration.

## Portability

When imported, SignalWorks Studio matches signal names against the current CSV. Missing signals are ignored for that dataset. Reference Lines and Range Bands do not depend on signal names, so they remain available across compatible projects/logs.


## Backward compatibility

SignalWorks Studio V4.4.5 imports the current `SignalWorksStudioPreset` format and also accepts legacy `GraphPlotSignalPreset` and `CSVDataPlotterPreset` V1 files. Existing presets therefore remain usable after the branding change.
