# rules_bc.py

from pyke import contexts, pattern, bc_rule

pyke_version = '1.1.1'
compiler_version = 1

def what_to_buy_tesla(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('facts', 'electric', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "rules.what_to_buy_tesla: got unexpected plan from when clause 1"
            rule.rule_base.num_bc_rule_successes += 1
            yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def what_to_buy_ford(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('facts', 'electric', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "rules.what_to_buy_ford: got unexpected plan from when clause 1"
            rule.rule_base.num_bc_rule_successes += 1
            yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def populate(engine):
  This_rule_base = engine.get_create('rules')
  
  bc_rule.bc_rule('what_to_buy_tesla', This_rule_base, 'what_to_buy',
                  what_to_buy_tesla, None,
                  (pattern.pattern_literal('tesla'),),
                  (),
                  (pattern.pattern_literal(True),))
  
  bc_rule.bc_rule('what_to_buy_ford', This_rule_base, 'what_to_buy',
                  what_to_buy_ford, None,
                  (pattern.pattern_literal('ford'),),
                  (),
                  (pattern.pattern_literal(False),))


Krb_filename = '..\\rules.krb'
Krb_lineno_map = (
    ((14, 18), (4, 4)),
    ((20, 25), (6, 6)),
    ((38, 42), (9, 9)),
    ((44, 49), (11, 11)),
)
