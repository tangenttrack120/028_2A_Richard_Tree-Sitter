/**
 * @file Filter grammar for tree-sitter
 * @author Tangenttrack120
 * @license MIT
 */

/// <reference types="tree-sitter-cli/dsl" />
// @ts-check

export default grammar({
  name: "filter",
  extras: ($) => [/\s/],
  rules: {
    query: ($) => $.comparison,
    comparison: ($) => seq($.identifier, "=", $.string),
    identifier: ($) => /[a-zA-Z_][a-zA-Z0-9_.]*/,
    string: ($) => /"[^"]*"/,
  },
});
