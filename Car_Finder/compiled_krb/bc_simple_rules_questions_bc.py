# bc_simple_rules_questions_bc.py

from pyke import contexts, pattern, bc_rule

pyke_version = '1.1.1'
compiler_version = 1

def no_rain(rule, arg_patterns, arg_context):
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
        with engine.prove('questions', 'is_raining', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc_simple_rules_questions.no_rain: got unexpected plan from when clause 1"
            rule.rule_base.num_bc_rule_successes += 1
            yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def what_to_bring_raincoat(rule, arg_patterns, arg_context):
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
        with engine.prove('questions', 'is_raining', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc_simple_rules_questions.what_to_bring_raincoat: got unexpected plan from when clause 1"
            with engine.prove('questions', 'is_windy', context,
                              (rule.pattern(1),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "bc_simple_rules_questions.what_to_bring_raincoat: got unexpected plan from when clause 2"
                rule.rule_base.num_bc_rule_successes += 1
                yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def what_to_bring_umbrella(rule, arg_patterns, arg_context):
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
        with engine.prove('questions', 'is_raining', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc_simple_rules_questions.what_to_bring_umbrella: got unexpected plan from when clause 1"
            with engine.prove('questions', 'is_windy', context,
                              (rule.pattern(0),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "bc_simple_rules_questions.what_to_bring_umbrella: got unexpected plan from when clause 2"
                rule.rule_base.num_bc_rule_successes += 1
                yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def what_to_bring_marshmellos(rule, arg_patterns, arg_context):
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
        with engine.prove('questions', 'any_disasters', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc_simple_rules_questions.what_to_bring_marshmellos: got unexpected plan from when clause 1"
            if context.lookup_data('ans') in (1,):
              rule.rule_base.num_bc_rule_successes += 1
              yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def what_to_bring_kite(rule, arg_patterns, arg_context):
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
        with engine.prove('questions', 'any_disasters', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc_simple_rules_questions.what_to_bring_kite: got unexpected plan from when clause 1"
            if context.lookup_data('ans') in (2,3):
              rule.rule_base.num_bc_rule_successes += 1
              yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def what_to_bring_tissues(rule, arg_patterns, arg_context):
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
        with engine.prove('questions', 'any_disasters', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc_simple_rules_questions.what_to_bring_tissues: got unexpected plan from when clause 1"
            if context.lookup_data('ans') in (4,):
              rule.rule_base.num_bc_rule_successes += 1
              yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def populate(engine):
  This_rule_base = engine.get_create('bc_simple_rules_questions')
  
  bc_rule.bc_rule('no_rain', This_rule_base, 'what_to_bring',
                  no_rain, None,
                  (pattern.pattern_literal('no_rain_gear'),),
                  (),
                  (pattern.pattern_literal(False),))
  
  bc_rule.bc_rule('what_to_bring_raincoat', This_rule_base, 'what_to_bring',
                  what_to_bring_raincoat, None,
                  (pattern.pattern_literal('raincoat'),),
                  (),
                  (pattern.pattern_literal(True),
                   pattern.pattern_literal(False),))
  
  bc_rule.bc_rule('what_to_bring_umbrella', This_rule_base, 'what_to_bring',
                  what_to_bring_umbrella, None,
                  (pattern.pattern_literal('umbrella'),),
                  (),
                  (pattern.pattern_literal(True),))
  
  bc_rule.bc_rule('what_to_bring_marshmellos', This_rule_base, 'what_to_bring',
                  what_to_bring_marshmellos, None,
                  (pattern.pattern_literal('marshmellos'),),
                  (),
                  (contexts.variable('ans'),))
  
  bc_rule.bc_rule('what_to_bring_kite', This_rule_base, 'what_to_bring',
                  what_to_bring_kite, None,
                  (pattern.pattern_literal('kite'),),
                  (),
                  (contexts.variable('ans'),))
  
  bc_rule.bc_rule('what_to_bring_tissues', This_rule_base, 'what_to_bring',
                  what_to_bring_tissues, None,
                  (pattern.pattern_literal('tissues'),),
                  (),
                  (contexts.variable('ans'),))


Krb_filename = '..\\bc_simple_rules_questions.krb'
Krb_lineno_map = (
    ((14, 18), (4, 4)),
    ((20, 25), (6, 6)),
    ((38, 42), (9, 9)),
    ((44, 49), (11, 11)),
    ((50, 55), (12, 12)),
    ((68, 72), (15, 15)),
    ((74, 79), (17, 17)),
    ((80, 85), (18, 18)),
    ((98, 102), (21, 21)),
    ((104, 109), (23, 23)),
    ((110, 110), (24, 24)),
    ((123, 127), (27, 27)),
    ((129, 134), (29, 29)),
    ((135, 135), (30, 30)),
    ((148, 152), (33, 33)),
    ((154, 159), (35, 35)),
    ((160, 160), (36, 36)),
)
