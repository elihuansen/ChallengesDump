from termcolor import colored

class GradingPrinter:
    def __init__(self, line_delimiter='|'):
        self.line_delimiter = line_delimiter
        self.header = ('Expected', 'Actual')
        self.expected_col = []
        self.actual_col   = []
        
        self.max_left  = len(self.header[0])
        self.max_right = len(self.header[1])

    def __iadd__(self, message):
        self.write(message)
        return self

    def write(self, expected_vs_actual):

        expected, actual = expected_vs_actual

        len_expected, len_actual = len(str(expected)), len(str(actual))

        if len_expected > self.max_left:
            self.max_left = len_expected
        
        if len_actual > self.max_right:
            self.max_right = len_actual

        self.expected_col.append(expected)
        self.actual_col.append(actual)

    def print(self):
        self._print_header()
        self._print_body()

    def _print_header(self):
        left_header, right_header = self.header
        left_header = left_header.rjust(self.max_left)

        header_line = '-' * (self.max_left) + ' | ' + '-' * self.max_right 

        print(colored(left_header, 'yellow'), colored(self.line_delimiter, 'grey'), colored(right_header, 'cyan'))
        print(colored(header_line, 'grey'))

    def _print_body(self):
        for expected_output, actual_output in zip(self.expected_col, self.actual_col):
            correctness_color = self._correctness_color_from_comparing(expected_output, actual_output)
            
            expected_output = str(expected_output).rjust(self.max_left)
            print(colored(expected_output, 'yellow'), colored(self.line_delimiter, 'grey'),  colored(actual_output, correctness_color))

    def _correctness_color_from_comparing(self, left_msg, right_msg):
        return 'green' if left_msg == right_msg else 'red'