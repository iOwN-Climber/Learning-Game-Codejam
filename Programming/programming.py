import pygame
import random


class Programming:

    def __init__(self, win, bps, bps_a, bps_b, bps_c, bps_l):
        self.win = win
        self.bps = bps
        self.bps_a = bps_a
        self.bps_b = bps_b
        self.bps_c = bps_c
        self.bps_l = bps_l

        self.WHITE = (255, 255, 255)
        self.BLACK = (0, 0, 0)
        self.RED = (255, 0, 0)
        self.GREEN = (0, 230, 60)

        self.font_answers = pygame.font.SysFont("helvetica", 25)
        self.font_answer_answer = pygame.font.SysFont("helvetica", 35)
        self.font_title = pygame.font.SysFont("helvetica", 40)

        self.tasks = {'my_list = ["Hi", 1, "School"]\n'
                      'new_list = my_list\n'

                      'my_list[0] = "hello"\n'
                      'new_list.append(7)\n'
                      'print(my_list)': ["['hello', 1, 'School']", "['hello', 1, 'School', 7]", "['hi', 1, 'School']",
                                         1],

                      'my_string = "foo ba"\n'
                      'k = [(i.upper(), len(i)) for i in my_string]\n'
                      'print(k)': ["[('FOO',3),(BA',2)]", "[('F',1),('O',1),('O',1),(' ',1),('B',1),('A',1)",
                                   "[('FOO BA',6)]", 1],

                      'def math(a, b):\n'
                      'x = a + b * a ** 2\n'
                      'return x\n'
                      '\n'
                      'math(3, 5)\n': ["48", "17", "No Output", 2],

                      'def creator(food, drink="Coke"):\n'
                      'lunch = food + drink\n'
                      'return lunch\n'
                      '\n'
                      'print(creator("Pizza))\n': ["PizzaCoke", "Pizza Coke", "Error, missing one required argument", 0]
                      }

        self.tasks_list = []
        self.task = None
        self.task_num = random.choice((0, len(self.tasks_list)))
        self.answer = None
        self.count = 0
        self.a = False
        self.b = False
        self.c = False
        self.done = False

    def back_home(self):
        if self.done:
            self.done = False
            return True
        return False

    def update_task_num(self):
        if len(self.tasks) > 0:
            self.create_tasks_list()
            self.task_num = random.choice((0, len(self.tasks_list) - 1))
            return True
        return False

    def create_tasks_list(self):
        for key in self.tasks:
            self.tasks_list.append(key)

    def answer_rect(self, width, height, x, y):
        pygame.draw.rect(self.win, self.BLACK, (x, y, width, height))

    def choose_task(self):
        self.task = self.tasks_list[self.task_num]
        self.task = list(self.task.split("\n"))
        return self.task

    def draw_task(self, x, y):
        add_y = 0
        for i in self.task:
            answer = self.font_answers.render(i, 1, self.BLACK)
            self.win.blit(answer, (x, y + add_y))
            add_y += answer.get_height() + 5

    def draw_ans(self, x, y, y2, y3):

        ans1, ans2, ans3, correct_ans = self.tasks[self.tasks_list[self.task_num]]

        ans1_text = self.font_answers.render(ans1, True, self.BLACK)
        self.win.blit(ans1_text, (x, y))

        ans2_text = self.font_answers.render(ans2, True, self.BLACK)
        self.win.blit(ans2_text, (x, y2))

        ans3_text = self.font_answers.render(ans3, True, self.BLACK)
        self.win.blit(ans3_text, (x, y3))

    def choose_answer(self, a=False, b=False, c=False):
        if a:
            self.answer = 0
            self.a = True
            self.b = False
            self.c = False
            return self.a
        elif b:
            self.answer = 1
            self.a = False
            self.b = True
            self.c = False
            return self.b
        elif c:
            self.answer = 2
            self.a = False
            self.b = False
            self.c = True
            return self.c
        else:
            self.answer = None
            self.a = False
            self.b = False
            self.c = None

    def check_answer(self):
        if self.answer is None:
            no_answer_text = self.font_answer_answer.render("Please choose an answer!", True, self.RED)
            self.win.blit(no_answer_text, (270, 380))
            pygame.display.update()
            pygame.time.delay(1000)
            self.choose_answer()
        elif self.answer == self.tasks[self.tasks_list[self.task_num]][3]:
            win_text = self.font_answer_answer.render("Correct!", True, self.GREEN)
            self.win.blit(win_text, (270, 380))
            pygame.display.update()
            del self.tasks[self.tasks_list[self.task_num]]
            self.tasks_list.remove(self.tasks_list[self.task_num])
            pygame.time.delay(1000)
            self.choose_answer()
            self.count += 1
            if self.update_task_num():
                self.choose_task()
        else:
            loose_text = self.font_answer_answer.render("Wrong!", True, self.RED)
            self.win.blit(loose_text, (270, 380))
            pygame.display.update()
            pygame.time.delay(1000)
            self.choose_answer()

    def draw(self):
        if len(self.tasks) > 0:
            if self.a:
                self.win.blit(self.bps_a, (0, 0))
            elif self.b:
                self.win.blit(self.bps_b, (0, 0))
            elif self.c:
                self.win.blit(self.bps_c, (0, 0))
            else:
                self.win.blit(self.bps, (0, 0))
            if self.count > 1 or self.count == 0:
                correct_answers = self.font_answers.render(f"You have {self.count} correct answers!", True, self.BLACK)
                self.win.blit(correct_answers, (270, 450))
            else:
                correct_answers = self.font_answers.render(f"You have {self.count} correct answer!", True, self.BLACK)
                self.win.blit(correct_answers, (270, 450))
            title = self.font_title.render("What is the output of the following code?", True, self.BLACK)
            self.win.blit(title, ((820 - 583) // 2 + 240, 80))
            if len(self.tasks) > 0:
                self.draw_task(270, 150)
                self.draw_ans(700, 133, 233, 333)
        else:
            self.win.blit(self.bps_l, (0, 0))
            finished_text = self.font_title.render("You already solved all tasks", True, self.BLACK)
            self.win.blit(finished_text, (250, 125))
            finished_text = self.font_title.render("You will be moved to the home screen in 3 seconds!", True,
                                                   self.BLACK)
            self.win.blit(finished_text, (250, 125 + 5 + finished_text.get_height()))
            pygame.display.update()
            pygame.time.delay(3000)
            self.done = True
            return
