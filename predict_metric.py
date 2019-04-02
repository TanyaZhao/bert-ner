import os
import codecs

def get_perf_metric(eval_path, config, best_f1):
    """
    checked
    Evalute the result file and get the new f1 value
    :param name: name of the model
    :param best_f1: the current best f1 value
    :return: new best f1 value, the new f1 value, whether the new best f1 value is updated
    """
    should_save = False
    new_f1 = 0.0

    prediction_file = os.path.join(eval_path, "%s.predict" % config['predict']['dataset'])
    score_file = os.path.join(eval_path, "%s.score" % config['predict']['dataset'])
    eval_script = "data/eval.pl"

    os.system('perl %s <%s >%s' % (eval_script, prediction_file, score_file))

    evaluation_lines = [line.rstrip() for line in codecs.open(score_file, 'r', 'utf8')]

    for i, line in enumerate(evaluation_lines):
        if i == 1:
            new_f1 = float(line.strip().split()[-1])
            if new_f1 > best_f1:
                best_f1 = new_f1
                should_save = True

    return new_f1, should_save