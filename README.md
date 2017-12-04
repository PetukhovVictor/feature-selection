# feature-selection

Program for feature selection using feature frequncy information.

## Program arguments

- --input (i-): input file with feature list sorted by frequncy
- --output (o-): output file with selected feature list

## Supported feature selectors

### Ends selector

This selector can select features from head or tail of features with sorting by frequncy.

#### Types
- head: cut features from head features list with sorting by frequncy;
- tail: cut features from tail features list with sorting by frequncy.

#### Parameters
- **by = 'value'**: feature selection with specified value bound after or before which features will be selected;
- **by = 'order'**: same, but order bound;
- **bound**: value or order bound after or before which features will be selected.

#### Examples
```
{
    'type': 'tail',
    'params': {
        'by': 'value',
        'bound': 50
    }
}
```
```
{
    'type': 'head',
    'params': {
        'by': 'value',
        'bound': 50000
    }
}
```

### Derivative bounds selector

This selector can clipping features whose values mapped to the values of the derivative, which do not exceed a specified distance from the specified point ( e.g. tan(Pi / 4) ).

#### Parameters
- **point**: the point from which the deviation of the derivative will be calculated;
- **deviation** = max derivative deviation.

#### Examples
```
{
    'type': 'derivative_bounds',
    'params': {
        'point': math.tan(math.pi / 4),
        'deviation': 0.5
    }
}
```

## Input data

Program required features list with sorting by frequncy (list of pair: feature name and feature value).

Example:
```
[
  ["BLOCK:POSTFIX_EXPRESSION:SAFE_ACCESS_EXPRESSION", 50],
  ["BLOCK:POSTFIX_EXPRESSION:SAFE_ACCESS", 1643],
  ["FUN:VALUE_ARGUMENT:IF", 12445],
  ["PROPERTY:TYPE_PROJECTION:FUNCTION_TYPE", 22],
  ["PROPERTY:TYPE_PROJECTION:VALUE_PARAMETER_LIST", 934],
  ["PROPERTY:TYPE_PROJECTION:ARROW", 141234],
  ["BINARY_EXPRESSION:VALUE_ARGUMENT_LIST:if", 335],
  ["BINARY_EXPRESSION:VALUE_ARGUMENT_LIST:CONDITION", 901],
  ["BINARY_EXPRESSION:VALUE_ARGUMENT_LIST:THEN", 1153],
  ["BINARY_EXPRESSION:VALUE_ARGUMENT_LIST:else", 5043]
]
```

## Output data

Selected feature list of same format.
