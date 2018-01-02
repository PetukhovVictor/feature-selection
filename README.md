# feature-selection

Program for feature selection using feature frequncy information.

## Program arguments

- **--input (i-)**: input file with features map
- **--output (o-)**: output file with selected feature list

Example of use:
```
python3 main.py -i features.json -o features_selected.json
```

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

Program required features map: "feature name" - "feature value".

Example:
```
{
   "RETURN:DOT_QUALIFIED_EXPRESSION:IDENTIFIER":47575,
   "THEN:DOT_QUALIFIED_EXPRESSION:IDENTIFIER":74185,
   "THEN:RETURN:IDENTIFIER":4111,
   "IF:RETURN:IDENTIFIER":4620,
   "RETURN:DOT":19444,
   "RETURN:DOT_QUALIFIED_EXPRESSION:DOT":34104,
   "THEN:DOT_QUALIFIED_EXPRESSION:DOT":46137,
   "RETURN:VALUE_ARGUMENT_LIST:REFERENCE_EXPRESSION":39958,
   "RETURN:VALUE_ARGUMENT_LIST:RPAR":22982,
   "RETURN:CALL_EXPRESSION:RPAR":27579,
   "THEN:RBRACE":33671,
   "IF:RBRACE":41584,
   "THEN:BLOCK:RBRACE":34530,
   "IF:BLOCK:RBRACE":42313,
   "BLOCK:BLOCK:RBRACE":55548,
   "BLOCK:RETURN:if":1468,
   "RETURN:IF:WHITE_SPACE":12403,
   "RETURN:LPAR":14068,
   "RETURN:IF:LPAR":1748,
   "BLOCK:RETURN:LPAR":14361,
   "RETURN:CONDITION":1442,
   "RETURN:IF:CONDITION":1738,
   "BLOCK:RETURN:CONDITION":1468
}
```

## Output data

Selected feature list of pair: feature name and feature value
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