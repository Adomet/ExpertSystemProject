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
            with engine.prove('facts', 'cheap', context,
                              (rule.pattern(1),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "rules.what_to_buy_tesla: got unexpected plan from when clause 2"
                with engine.prove('facts', 'type4x4', context,
                                  (rule.pattern(0),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "rules.what_to_buy_tesla: got unexpected plan from when clause 3"
                    with engine.prove('facts', 'manuel', context,
                                      (rule.pattern(1),)) \
                      as gen_4:
                      for x_4 in gen_4:
                        assert x_4 is None, \
                          "rules.what_to_buy_tesla: got unexpected plan from when clause 4"
                        with engine.prove('facts', 'seat4', context,
                                          (rule.pattern(0),)) \
                          as gen_5:
                          for x_5 in gen_5:
                            assert x_5 is None, \
                              "rules.what_to_buy_tesla: got unexpected plan from when clause 5"
                            with engine.prove('facts', 'sedan', context,
                                              (rule.pattern(0),)) \
                              as gen_6:
                              for x_6 in gen_6:
                                assert x_6 is None, \
                                  "rules.what_to_buy_tesla: got unexpected plan from when clause 6"
                                with engine.prove('facts', 'horsepower', context,
                                                  (rule.pattern(0),)) \
                                  as gen_7:
                                  for x_7 in gen_7:
                                    assert x_7 is None, \
                                      "rules.what_to_buy_tesla: got unexpected plan from when clause 7"
                                    with engine.prove('facts', 'offroad', context,
                                                      (rule.pattern(1),)) \
                                      as gen_8:
                                      for x_8 in gen_8:
                                        assert x_8 is None, \
                                          "rules.what_to_buy_tesla: got unexpected plan from when clause 8"
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
            with engine.prove('facts', 'cheap', context,
                              (rule.pattern(0),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "rules.what_to_buy_ford: got unexpected plan from when clause 2"
                with engine.prove('facts', 'type4x4', context,
                                  (rule.pattern(0),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "rules.what_to_buy_ford: got unexpected plan from when clause 3"
                    with engine.prove('facts', 'manuel', context,
                                      (rule.pattern(1),)) \
                      as gen_4:
                      for x_4 in gen_4:
                        assert x_4 is None, \
                          "rules.what_to_buy_ford: got unexpected plan from when clause 4"
                        with engine.prove('facts', 'seat4', context,
                                          (rule.pattern(1),)) \
                          as gen_5:
                          for x_5 in gen_5:
                            assert x_5 is None, \
                              "rules.what_to_buy_ford: got unexpected plan from when clause 5"
                            with engine.prove('facts', 'sedan', context,
                                              (rule.pattern(1),)) \
                              as gen_6:
                              for x_6 in gen_6:
                                assert x_6 is None, \
                                  "rules.what_to_buy_ford: got unexpected plan from when clause 6"
                                with engine.prove('facts', 'horsepower', context,
                                                  (rule.pattern(1),)) \
                                  as gen_7:
                                  for x_7 in gen_7:
                                    assert x_7 is None, \
                                      "rules.what_to_buy_ford: got unexpected plan from when clause 7"
                                    with engine.prove('facts', 'offroad', context,
                                                      (rule.pattern(1),)) \
                                      as gen_8:
                                      for x_8 in gen_8:
                                        assert x_8 is None, \
                                          "rules.what_to_buy_ford: got unexpected plan from when clause 8"
                                        rule.rule_base.num_bc_rule_successes += 1
                                        yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def what_to_buy_sahin(rule, arg_patterns, arg_context):
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
              "rules.what_to_buy_sahin: got unexpected plan from when clause 1"
            with engine.prove('facts', 'cheap', context,
                              (rule.pattern(1),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "rules.what_to_buy_sahin: got unexpected plan from when clause 2"
                with engine.prove('facts', 'type4x4', context,
                                  (rule.pattern(0),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "rules.what_to_buy_sahin: got unexpected plan from when clause 3"
                    with engine.prove('facts', 'manuel', context,
                                      (rule.pattern(1),)) \
                      as gen_4:
                      for x_4 in gen_4:
                        assert x_4 is None, \
                          "rules.what_to_buy_sahin: got unexpected plan from when clause 4"
                        with engine.prove('facts', 'seat4', context,
                                          (rule.pattern(1),)) \
                          as gen_5:
                          for x_5 in gen_5:
                            assert x_5 is None, \
                              "rules.what_to_buy_sahin: got unexpected plan from when clause 5"
                            with engine.prove('facts', 'sedan', context,
                                              (rule.pattern(1),)) \
                              as gen_6:
                              for x_6 in gen_6:
                                assert x_6 is None, \
                                  "rules.what_to_buy_sahin: got unexpected plan from when clause 6"
                                with engine.prove('facts', 'horsepower', context,
                                                  (rule.pattern(1),)) \
                                  as gen_7:
                                  for x_7 in gen_7:
                                    assert x_7 is None, \
                                      "rules.what_to_buy_sahin: got unexpected plan from when clause 7"
                                    with engine.prove('facts', 'offroad', context,
                                                      (rule.pattern(1),)) \
                                      as gen_8:
                                      for x_8 in gen_8:
                                        assert x_8 is None, \
                                          "rules.what_to_buy_sahin: got unexpected plan from when clause 8"
                                        rule.rule_base.num_bc_rule_successes += 1
                                        yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def what_to_buy_supra(rule, arg_patterns, arg_context):
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
              "rules.what_to_buy_supra: got unexpected plan from when clause 1"
            with engine.prove('facts', 'cheap', context,
                              (rule.pattern(0),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "rules.what_to_buy_supra: got unexpected plan from when clause 2"
                with engine.prove('facts', 'type4x4', context,
                                  (rule.pattern(0),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "rules.what_to_buy_supra: got unexpected plan from when clause 3"
                    with engine.prove('facts', 'manuel', context,
                                      (rule.pattern(1),)) \
                      as gen_4:
                      for x_4 in gen_4:
                        assert x_4 is None, \
                          "rules.what_to_buy_supra: got unexpected plan from when clause 4"
                        with engine.prove('facts', 'seat4', context,
                                          (rule.pattern(0),)) \
                          as gen_5:
                          for x_5 in gen_5:
                            assert x_5 is None, \
                              "rules.what_to_buy_supra: got unexpected plan from when clause 5"
                            with engine.prove('facts', 'sedan', context,
                                              (rule.pattern(1),)) \
                              as gen_6:
                              for x_6 in gen_6:
                                assert x_6 is None, \
                                  "rules.what_to_buy_supra: got unexpected plan from when clause 6"
                                with engine.prove('facts', 'horsepower', context,
                                                  (rule.pattern(1),)) \
                                  as gen_7:
                                  for x_7 in gen_7:
                                    assert x_7 is None, \
                                      "rules.what_to_buy_supra: got unexpected plan from when clause 7"
                                    with engine.prove('facts', 'offroad', context,
                                                      (rule.pattern(0),)) \
                                      as gen_8:
                                      for x_8 in gen_8:
                                        assert x_8 is None, \
                                          "rules.what_to_buy_supra: got unexpected plan from when clause 8"
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
                  (pattern.pattern_literal(True),
                   pattern.pattern_literal(False),))
  
  bc_rule.bc_rule('what_to_buy_ford', This_rule_base, 'what_to_buy',
                  what_to_buy_ford, None,
                  (pattern.pattern_literal('ford'),),
                  (),
                  (pattern.pattern_literal(False),
                   pattern.pattern_literal(True),))
  
  bc_rule.bc_rule('what_to_buy_sahin', This_rule_base, 'what_to_buy',
                  what_to_buy_sahin, None,
                  (pattern.pattern_literal('sahin'),),
                  (),
                  (pattern.pattern_literal(False),
                   pattern.pattern_literal(True),))
  
  bc_rule.bc_rule('what_to_buy_supra', This_rule_base, 'what_to_buy',
                  what_to_buy_supra, None,
                  (pattern.pattern_literal('supra'),),
                  (),
                  (pattern.pattern_literal(False),
                   pattern.pattern_literal(True),))


Krb_filename = '..\\rules.krb'
Krb_lineno_map = (
    ((14, 18), (4, 4)),
    ((20, 25), (6, 6)),
    ((26, 31), (7, 7)),
    ((32, 37), (8, 8)),
    ((38, 43), (9, 9)),
    ((44, 49), (10, 10)),
    ((50, 55), (11, 11)),
    ((56, 61), (12, 12)),
    ((62, 67), (13, 13)),
    ((80, 84), (16, 16)),
    ((86, 91), (18, 18)),
    ((92, 97), (19, 19)),
    ((98, 103), (20, 20)),
    ((104, 109), (21, 21)),
    ((110, 115), (22, 22)),
    ((116, 121), (23, 23)),
    ((122, 127), (24, 24)),
    ((128, 133), (25, 25)),
    ((146, 150), (28, 28)),
    ((152, 157), (30, 30)),
    ((158, 163), (31, 31)),
    ((164, 169), (32, 32)),
    ((170, 175), (33, 33)),
    ((176, 181), (34, 34)),
    ((182, 187), (35, 35)),
    ((188, 193), (36, 36)),
    ((194, 199), (37, 37)),
    ((212, 216), (40, 40)),
    ((218, 223), (42, 42)),
    ((224, 229), (43, 43)),
    ((230, 235), (44, 44)),
    ((236, 241), (45, 45)),
    ((242, 247), (46, 46)),
    ((248, 253), (47, 47)),
    ((254, 259), (48, 48)),
    ((260, 265), (49, 49)),
)
