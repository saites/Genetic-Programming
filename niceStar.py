from robot import *
from world import *

w = World('resources/star.bmp')
robot = Robot(w, 40, 41)

from viewer import *
from pygame.locals import *
import sys
import pygame

v = Viewer(w,560,360)
v.addRobot(robot)
v.draw()

while(True):
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			print robot.getScore()
			sys.exit()
		elif event.type == KEYDOWN and event.key == K_ESCAPE:
			pygame.event.post(pygame.event.Event(QUIT))
	if robot.getView()[0,0]:
		robot.moveLeft()
		if robot.getView()[0,2]:
			robot.moveLeft()
			if robot.getView()[0,2]:
				if robot.getView()[1,0]:
					if robot.getView()[2,2]:
						robot.moveRight()
						if robot.getView()[1,2]:
							robot.moveUp()
							if robot.getView()[1,0]:
								robot.moveUp()
								if robot.getView()[2,2]:
									robot.moveRight()
									if robot.getView()[1,2]:
										if robot.getView()[1,2]:
											robot.moveRight()
											robot.moveUp()
											if robot.getView()[2,2]:
												robot.moveRight()
												if robot.getView()[1,2]:
													pass
												else:
													robot.moveRight()
											else:
												robot.moveUp()
												robot.moveRight()
										else:
											robot.moveLeft()
											robot.moveDown()
											robot.moveDown()
											if robot.getView()[1,2]:
												if robot.getView()[2,1]:
													robot.moveRight()
													if robot.getView()[0,2]:
														robot.moveRight()
														robot.moveDown()
														if robot.getView()[1,2]:
															if robot.getView()[2,1]:
																pass
															else:
																robot.moveRight()
																robot.moveUp()
														else:
															robot.moveUp()
															if robot.getView()[0,2]:
																pass
															else:
																pass
													else:
														pass
												else:
													robot.moveUp()
											else:
												robot.moveUp()
												robot.moveDown()
									else:
										if robot.getView()[1,0]:
											robot.moveUp()
											if robot.getView()[1,0]:
												robot.moveUp()
												robot.moveUp()
												if robot.getView()[1,2]:
													robot.moveLeft()
													robot.moveUp()
													if robot.getView()[1,2]:
														robot.moveUp()
														robot.moveRight()
														robot.moveRight()
														robot.moveRight()
														robot.moveUp()
													else:
														robot.moveRight()
														robot.moveDown()
														robot.moveRight()
														robot.moveLeft()
														robot.moveDown()
														robot.moveRight()
												else:
													robot.moveRight()
													if robot.getView()[1,2]:
														pass
													else:
														robot.moveLeft()
														robot.moveRight()
														if robot.getView()[2,2]:
															if robot.getView()[1,2]:
																robot.moveRight()
																robot.moveDown()
																robot.moveUp()
																robot.moveRight()
															else:
																robot.moveLeft()
																robot.moveDown()
																if robot.getView()[2,2]:
																	pass
																else:
																	robot.moveLeft()
														else:
															if robot.getView()[0,1]:
																if robot.getView()[1,2]:
																	if robot.getView()[1,2]:
																		robot.moveRight()
																		robot.moveUp()
																		if robot.getView()[2,1]:
																			if robot.getView()[1,2]:
																				pass
																			else:
																				if robot.getView()[0,0]:
																					robot.moveRight()
																					robot.moveDown()
																				else:
																					pass
																		else:
																			if robot.getView()[0,1]:
																				robot.moveRight()
																			else:
																				robot.moveLeft()
																				if robot.getView()[2,1]:
																					pass
																				else:
																					pass
																	else:
																		robot.moveLeft()
																		robot.moveDown()
																		robot.moveDown()
																		if robot.getView()[1,2]:
																			if robot.getView()[2,1]:
																				robot.moveRight()
																				if robot.getView()[0,2]:
																					robot.moveRight()
																					if robot.getView()[1,2]:
																						robot.moveRight()
																						robot.moveUp()
																						if robot.getView()[1,2]:
																							robot.moveUp()
																							robot.moveRight()
																							robot.moveRight()
																							robot.moveRight()
																							robot.moveUp()
																							robot.moveDown()
																							robot.moveUp()
																							robot.moveLeft()
																						else:
																							robot.moveRight()
																							robot.moveDown()
																							robot.moveRight()
																							if robot.getView()[0,1]:
																								robot.moveRight()
																								robot.moveRight()
																								robot.moveUp()
																								robot.moveUp()
																								if robot.getView()[0,2]:
																									pass
																								else:
																									if robot.getView()[1,2]:
																										if robot.getView()[1,2]:
																											robot.moveRight()
																											robot.moveUp()
																										else:
																											robot.moveLeft()
																											robot.moveLeft()
																											robot.moveRight()
																									else:
																										if robot.getView()[1,0]:
																											robot.moveUp()
																											if robot.getView()[1,0]:
																												robot.moveUp()
																												robot.moveUp()
																												if robot.getView()[1,2]:
																													robot.moveUp()
																													robot.moveRight()
																													robot.moveDown()
																												else:
																													robot.moveRight()
																													if robot.getView()[1,2]:
																														pass
																													else:
																														robot.moveLeft()
																														robot.moveUp()
																														robot.moveRight()
																											else:
																												pass
																										else:
																											robot.moveLeft()
																											robot.moveLeft()
																											robot.moveLeft()
																											robot.moveDown()
																							else:
																								robot.moveLeft()
																								if robot.getView()[1,0]:
																									robot.moveUp()
																									if robot.getView()[2,2]:
																										robot.moveRight()
																										robot.moveLeft()
																										robot.moveDown()
																										if robot.getView()[0,0]:
																											robot.moveRight()
																											robot.moveUp()
																										else:
																											pass
																									else:
																										if robot.getView()[0,1]:
																											robot.moveRight()
																										else:
																											robot.moveLeft()
																								else:
																									pass
																					else:
																						robot.moveLeft()
																						robot.moveDown()
																						if robot.getView()[2,2]:
																							pass
																						else:
																							robot.moveLeft()
																							robot.moveUp()
																				else:
																					pass
																			else:
																				robot.moveUp()
																		else:
																			robot.moveUp()
																			robot.moveDown()
																else:
																	if robot.getView()[1,0]:
																		robot.moveUp()
																		if robot.getView()[1,0]:
																			robot.moveUp()
																			robot.moveUp()
																			if robot.getView()[1,2]:
																				robot.moveLeft()
																				robot.moveUp()
																				if robot.getView()[1,2]:
																					robot.moveUp()
																					robot.moveRight()
																					if robot.getView()[1,2]:
																						if robot.getView()[1,2]:
																							robot.moveRight()
																						else:
																							if robot.getView()[0,2]:
																								robot.moveUp()
																							else:
																								pass
																					else:
																						if robot.getView()[1,0]:
																							robot.moveLeft()
																							if robot.getView()[0,2]:
																								if robot.getView()[1,0]:
																									pass
																								else:
																									robot.moveUp()
																									if robot.getView()[0,1]:
																										robot.moveRight()
																										robot.moveLeft()
																										robot.moveDown()
																										robot.moveRight()
																									else:
																										robot.moveDown()
																							else:
																								robot.moveUp()
																								if robot.getView()[1,0]:
																									robot.moveUp()
																									robot.moveRight()
																									robot.moveDown()
																								else:
																									pass
																						else:
																							robot.moveLeft()
																							robot.moveRight()
																							robot.moveRight()
																							robot.moveUp()
																				else:
																					robot.moveRight()
																					robot.moveDown()
																					robot.moveRight()
																					robot.moveUp()
																					if robot.getView()[1,2]:
																						robot.moveUp()
																						robot.moveRight()
																						robot.moveRight()
																						robot.moveRight()
																						robot.moveUp()
																					else:
																						robot.moveRight()
																						robot.moveDown()
																						robot.moveRight()
																						if robot.getView()[0,2]:
																							pass
																						else:
																							pass
																			else:
																				robot.moveRight()
																				if robot.getView()[1,2]:
																					pass
																				else:
																					robot.moveLeft()
																					robot.moveRight()
																					if robot.getView()[2,2]:
																						if robot.getView()[1,2]:
																							robot.moveRight()
																							robot.moveDown()
																							robot.moveUp()
																							robot.moveRight()
																						else:
																							robot.moveLeft()
																							robot.moveDown()
																							robot.moveDown()
																							robot.moveUp()
																					else:
																						if robot.getView()[0,1]:
																							if robot.getView()[0,0]:
																								if robot.getView()[1,0]:
																									robot.moveUp()
																									robot.moveDown()
																									robot.moveDown()
																								else:
																									robot.moveDown()
																									if robot.getView()[1,0]:
																										robot.moveUp()
																									else:
																										pass
																							else:
																								if robot.getView()[1,2]:
																									pass
																								else:
																									robot.moveLeft()
																									robot.moveLeft()
																						else:
																							robot.moveRight()
																							if robot.getView()[1,2]:
																								pass
																							else:
																								pass
																		else:
																			pass
																	else:
																		robot.moveLeft()
																		robot.moveLeft()
															else:
																robot.moveRight()
																if robot.getView()[1,2]:
																	if robot.getView()[1,2]:
																		robot.moveRight()
																		if robot.getView()[1,0]:
																			robot.moveUp()
																		else:
																			robot.moveLeft()
																			robot.moveDown()
																			robot.moveRight()
																	else:
																		robot.moveLeft()
																		robot.moveDown()
																		if robot.getView()[1,2]:
																			if robot.getView()[2,1]:
																				robot.moveRight()
																				if robot.getView()[0,0]:
																					robot.moveLeft()
																					robot.moveDown()
																					if robot.getView()[1,0]:
																						robot.moveUp()
																						if robot.getView()[1,0]:
																							robot.moveUp()
																							robot.moveUp()
																							if robot.getView()[1,2]:
																								robot.moveUp()
																								if robot.getView()[1,0]:
																									robot.moveUp()
																								else:
																									pass
																							else:
																								robot.moveRight()
																								robot.moveLeft()
																								robot.moveDown()
																								if robot.getView()[2,2]:
																									robot.moveLeft()
																									robot.moveDown()
																									robot.moveDown()
																									robot.moveDown()
																									robot.moveLeft()
																									if robot.getView()[2,2]:
																										pass
																									else:
																										robot.moveDown()
																								else:
																									if robot.getView()[0,1]:
																										robot.moveRight()
																										robot.moveRight()
																										robot.moveDown()
																									else:
																										robot.moveLeft()
																						else:
																							pass
																					else:
																						robot.moveLeft()
																						robot.moveLeft()
																				else:
																					if robot.getView()[0,2]:
																						robot.moveRight()
																					else:
																						pass
																			else:
																				if robot.getView()[0,1]:
																					robot.moveDown()
																					if robot.getView()[1,2]:
																						if robot.getView()[2,1]:
																							robot.moveUp()
																						else:
																							robot.moveDown()
																							if robot.getView()[1,2]:
																								if robot.getView()[2,1]:
																									robot.moveRight()
																									robot.moveDown()
																									robot.moveDown()
																								else:
																									robot.moveUp()
																									if robot.getView()[0,2]:
																										robot.moveLeft()
																										robot.moveRight()
																										robot.moveUp()
																										robot.moveDown()
																										robot.moveUp()
																										robot.moveLeft()
																										robot.moveLeft()
																										if robot.getView()[0,0]:
																											robot.moveDown()
																											robot.moveDown()
																											robot.moveLeft()
																											robot.moveUp()
																											robot.moveDown()
																										else:
																											if robot.getView()[0,2]:
																												robot.moveRight()
																											else:
																												pass
																									else:
																										if robot.getView()[1,0]:
																											robot.moveDown()
																											robot.moveLeft()
																											robot.moveDown()
																											robot.moveDown()
																											if robot.getView()[1,2]:
																												if robot.getView()[1,0]:
																													robot.moveUp()
																												else:
																													pass
																											else:
																												pass
																										else:
																											pass
																							else:
																								robot.moveUp()
																								robot.moveDown()
																								robot.moveDown()
																								if robot.getView()[1,2]:
																									if robot.getView()[2,1]:
																										pass
																									else:
																										robot.moveRight()
																										robot.moveUp()
																								else:
																									if robot.getView()[2,2]:
																										robot.moveRight()
																										robot.moveDown()
																										robot.moveUp()
																										if robot.getView()[0,1]:
																											robot.moveRight()
																										else:
																											robot.moveRight()
																									else:
																										if robot.getView()[0,1]:
																											robot.moveRight()
																										else:
																											robot.moveLeft()
																					else:
																						robot.moveUp()
																						robot.moveUp()
																						robot.moveLeft()
																				else:
																					robot.moveDown()
																		else:
																			robot.moveUp()
																			robot.moveDown()
																			robot.moveUp()
																			if robot.getView()[1,2]:
																				if robot.getView()[0,0]:
																					pass
																				else:
																					robot.moveDown()
																					if robot.getView()[2,1]:
																						pass
																					else:
																						robot.moveRight()
																						robot.moveUp()
																						robot.moveRight()
																						robot.moveDown()
																						robot.moveUp()
																						robot.moveLeft()
																			else:
																				robot.moveLeft()
																				robot.moveDown()
																				robot.moveRight()
																				if robot.getView()[1,2]:
																					pass
																				else:
																					pass
																else:
																	pass
											else:
												pass
										else:
											robot.moveLeft()
											robot.moveLeft()
								else:
									if robot.getView()[0,1]:
										robot.moveRight()
										robot.moveLeft()
										if robot.getView()[2,2]:
											pass
										else:
											if robot.getView()[2,2]:
												pass
											else:
												robot.moveUp()
												robot.moveLeft()
									else:
										robot.moveLeft()
										if robot.getView()[1,0]:
											robot.moveRight()
											robot.moveLeft()
											robot.moveDown()
										else:
											pass
							else:
								pass
						else:
							pass
					else:
						if robot.getView()[0,1]:
							robot.moveUp()
							robot.moveDown()
							robot.moveRight()
						else:
							if robot.getView()[1,2]:
								if robot.getView()[2,1]:
									robot.moveRight()
									if robot.getView()[0,2]:
										robot.moveRight()
										robot.moveDown()
										if robot.getView()[1,2]:
											if robot.getView()[2,1]:
												pass
											else:
												robot.moveRight()
												robot.moveUp()
										else:
											robot.moveUp()
											robot.moveRight()
											robot.moveUp()
											robot.moveRight()
											robot.moveDown()
											robot.moveUp()
											if robot.getView()[0,1]:
												robot.moveRight()
												robot.moveRight()
												robot.moveUp()
												robot.moveDown()
												if robot.getView()[1,0]:
													pass
												else:
													robot.moveLeft()
													robot.moveDown()
													robot.moveRight()
											else:
												robot.moveLeft()
												if robot.getView()[1,0]:
													robot.moveUp()
													if robot.getView()[2,2]:
														robot.moveRight()
														robot.moveLeft()
														robot.moveDown()
														if robot.getView()[0,0]:
															robot.moveRight()
														else:
															pass
													else:
														if robot.getView()[0,1]:
															robot.moveRight()
														else:
															robot.moveLeft()
												else:
													pass
									else:
										pass
								else:
									robot.moveUp()
							else:
								robot.moveUp()
								robot.moveDown()
				else:
					robot.moveDown()
			else:
				if robot.getView()[1,2]:
					if robot.getView()[2,1]:
						pass
					else:
						robot.moveRight()
						robot.moveUp()
						robot.moveRight()
						robot.moveLeft()
						robot.moveDown()
						robot.moveDown()
				else:
					if robot.getView()[2,2]:
						robot.moveRight()
						robot.moveUp()
						if robot.getView()[1,2]:
							robot.moveUp()
							robot.moveRight()
							robot.moveDown()
						else:
							robot.moveRight()
							if robot.getView()[1,2]:
								pass
							else:
								robot.moveLeft()
								robot.moveUp()
								robot.moveRight()
					else:
						robot.moveRight()
						robot.moveLeft()
						if robot.getView()[2,2]:
							robot.moveDown()
							robot.moveRight()
						else:
							robot.moveLeft()
		else:
			if robot.getView()[0,2]:
				pass
			else:
				robot.moveRight()
				if robot.getView()[1,2]:
					robot.moveRight()
					if robot.getView()[1,2]:
						if robot.getView()[1,2]:
							robot.moveDown()
						else:
							robot.moveLeft()
							robot.moveRight()
					else:
						if robot.getView()[1,0]:
							robot.moveUp()
						else:
							robot.moveLeft()
							robot.moveDown()
							robot.moveUp()
							robot.moveDown()
							robot.moveUp()
							robot.moveLeft()
							robot.moveLeft()
							robot.moveLeft()
							if robot.getView()[0,2]:
								pass
							else:
								robot.moveLeft()
								robot.moveDown()
								robot.moveDown()
								robot.moveRight()
				else:
					if robot.getView()[1,0]:
						robot.moveLeft()
						robot.moveDown()
					else:
						robot.moveLeft()
						robot.moveRight()
						if robot.getView()[0,1]:
							robot.moveRight()
						else:
							if robot.getView()[2,2]:
								robot.moveRight()
								if robot.getView()[1,2]:
									if robot.getView()[1,2]:
										robot.moveRight()
										robot.moveUp()
										if robot.getView()[2,1]:
											if robot.getView()[1,2]:
												robot.moveUp()
												robot.moveLeft()
												robot.moveDown()
												robot.moveDown()
												if robot.getView()[0,1]:
													pass
												else:
													robot.moveLeft()
													if robot.getView()[0,2]:
														pass
													else:
														pass
											else:
												robot.moveRight()
												robot.moveDown()
												if robot.getView()[0,1]:
													pass
												else:
													robot.moveLeft()
													if robot.getView()[0,2]:
														pass
													else:
														pass
										else:
											if robot.getView()[0,1]:
												robot.moveRight()
											else:
												robot.moveLeft()
												if robot.getView()[2,1]:
													pass
												else:
													pass
									else:
										robot.moveLeft()
										robot.moveDown()
										robot.moveDown()
										if robot.getView()[1,2]:
											if robot.getView()[2,1]:
												robot.moveRight()
												if robot.getView()[0,2]:
													robot.moveLeft()
													robot.moveDown()
													robot.moveRight()
													if robot.getView()[1,2]:
														pass
													else:
														if robot.getView()[1,0]:
															robot.moveUp()
														else:
															robot.moveLeft()
												else:
													pass
											else:
												pass
										else:
											robot.moveUp()
								else:
									if robot.getView()[1,0]:
										robot.moveUp()
										if robot.getView()[1,0]:
											robot.moveUp()
											robot.moveUp()
											if robot.getView()[1,2]:
												robot.moveLeft()
												robot.moveUp()
												if robot.getView()[1,2]:
													robot.moveUp()
													robot.moveRight()
													robot.moveRight()
													robot.moveRight()
													robot.moveUp()
												else:
													robot.moveRight()
													robot.moveDown()
													robot.moveRight()
													if robot.getView()[0,2]:
														pass
													else:
														pass
											else:
												robot.moveRight()
												if robot.getView()[1,2]:
													pass
												else:
													robot.moveLeft()
													robot.moveRight()
													if robot.getView()[2,2]:
														if robot.getView()[1,2]:
															robot.moveRight()
															robot.moveDown()
															if robot.getView()[0,0]:
																robot.moveLeft()
																robot.moveDown()
																if robot.getView()[1,0]:
																	robot.moveLeft()
																	robot.moveDown()
																	robot.moveRight()
																	robot.moveLeft()
																	robot.moveRight()
																	if robot.getView()[0,1]:
																		robot.moveRight()
																	else:
																		robot.moveLeft()
																		if robot.getView()[0,2]:
																			if robot.getView()[2,2]:
																				robot.moveLeft()
																			else:
																				pass
																		else:
																			pass
																else:
																	robot.moveLeft()
																	if robot.getView()[2,2]:
																		robot.moveRight()
																	else:
																		if robot.getView()[1,0]:
																			robot.moveUp()
																		else:
																			pass
															else:
																if robot.getView()[0,2]:
																	robot.moveRight()
																else:
																	pass
														else:
															robot.moveLeft()
															robot.moveDown()
															robot.moveUp()
															robot.moveRight()
													else:
														if robot.getView()[0,1]:
															if robot.getView()[0,0]:
																if robot.getView()[1,0]:
																	robot.moveUp()
																	robot.moveDown()
																	robot.moveDown()
																else:
																	robot.moveDown()
																	robot.moveDown()
																	robot.moveRight()
																	robot.moveUp()
																	if robot.getView()[0,2]:
																		pass
																	else:
																		if robot.getView()[1,2]:
																			if robot.getView()[1,2]:
																				robot.moveRight()
																				robot.moveUp()
																				if robot.getView()[1,0]:
																					robot.moveUp()
																				else:
																					pass
																			else:
																				robot.moveLeft()
																				if robot.getView()[1,0]:
																					robot.moveUp()
																					robot.moveUp()
																				else:
																					robot.moveLeft()
																		else:
																			if robot.getView()[1,0]:
																				robot.moveUp()
																				if robot.getView()[1,0]:
																					robot.moveUp()
																					robot.moveLeft()
																				else:
																					pass
																			else:
																				robot.moveLeft()
																				robot.moveUp()
															else:
																robot.moveRight()
																robot.moveUp()
																if robot.getView()[0,1]:
																	robot.moveRight()
																else:
																	robot.moveLeft()
																	if robot.getView()[1,0]:
																		robot.moveUp()
																		if robot.getView()[2,2]:
																			robot.moveRight()
																			if robot.getView()[0,2]:
																				robot.moveUp()
																				if robot.getView()[1,0]:
																					if robot.getView()[1,0]:
																						robot.moveUp()
																						robot.moveUp()
																						robot.moveLeft()
																					else:
																						pass
																				else:
																					robot.moveLeft()
																			else:
																				pass
																		else:
																			robot.moveRight()
																	else:
																		robot.moveRight()
																		if robot.getView()[1,2]:
																			if robot.getView()[1,2]:
																				robot.moveRight()
																			else:
																				if robot.getView()[0,2]:
																					pass
																				else:
																					pass
																		else:
																			if robot.getView()[1,0]:
																				robot.moveLeft()
																				if robot.getView()[0,2]:
																					if robot.getView()[1,0]:
																						pass
																					else:
																						robot.moveDown()
																				else:
																					robot.moveUp()
																			else:
																				robot.moveLeft()
																				robot.moveRight()
																				if robot.getView()[0,1]:
																					robot.moveRight()
																					robot.moveRight()
																					robot.moveUp()
																					robot.moveUp()
																					if robot.getView()[0,2]:
																						pass
																					else:
																						if robot.getView()[1,2]:
																							if robot.getView()[1,2]:
																								robot.moveRight()
																								robot.moveUp()
																							else:
																								robot.moveLeft()
																								robot.moveLeft()
																								robot.moveRight()
																						else:
																							if robot.getView()[1,0]:
																								robot.moveUp()
																								if robot.getView()[1,0]:
																									robot.moveUp()
																									robot.moveUp()
																									if robot.getView()[1,2]:
																										robot.moveUp()
																										robot.moveRight()
																										robot.moveDown()
																									else:
																										robot.moveRight()
																										if robot.getView()[1,2]:
																											pass
																										else:
																											robot.moveLeft()
																											robot.moveUp()
																											robot.moveRight()
																								else:
																									pass
																							else:
																								robot.moveLeft()
																								robot.moveLeft()
																								robot.moveLeft()
																								robot.moveDown()
																				else:
																					pass
														else:
															robot.moveRight()
															if robot.getView()[1,2]:
																if robot.getView()[1,2]:
																	robot.moveRight()
																	robot.moveUp()
																	robot.moveDown()
																	robot.moveRight()
																	if robot.getView()[1,2]:
																		pass
																	else:
																		if robot.getView()[1,0]:
																			robot.moveUp()
																		else:
																			robot.moveLeft()
																else:
																	robot.moveLeft()
																	robot.moveDown()
																	if robot.getView()[1,2]:
																		if robot.getView()[2,1]:
																			robot.moveRight()
																			if robot.getView()[2,2]:
																				robot.moveRight()
																				robot.moveDown()
																				if robot.getView()[0,1]:
																					pass
																				else:
																					robot.moveLeft()
																					robot.moveUp()
																					robot.moveUp()
																					if robot.getView()[0,2]:
																						pass
																					else:
																						pass
																			else:
																				robot.moveLeft()
																				if robot.getView()[2,2]:
																					pass
																				else:
																					robot.moveLeft()
																		else:
																			if robot.getView()[0,1]:
																				robot.moveRight()
																			else:
																				robot.moveLeft()
																				robot.moveRight()
																				robot.moveRight()
																				robot.moveRight()
																				robot.moveUp()
																				if robot.getView()[0,2]:
																					robot.moveRight()
																				else:
																					pass
																	else:
																		robot.moveUp()
																		robot.moveDown()
																		robot.moveUp()
																		if robot.getView()[1,2]:
																			if robot.getView()[0,0]:
																				pass
																			else:
																				robot.moveDown()
																				if robot.getView()[2,1]:
																					pass
																				else:
																					pass
																		else:
																			robot.moveLeft()
																			robot.moveDown()
																			robot.moveRight()
																			if robot.getView()[1,2]:
																				pass
																			else:
																				pass
															else:
																pass
										else:
											pass
									else:
										robot.moveLeft()
										robot.moveLeft()
							else:
								if robot.getView()[0,1]:
									robot.moveRight()
									robot.moveLeft()
									if robot.getView()[2,2]:
										robot.moveUp()
									else:
										robot.moveLeft()
										robot.moveRight()
										robot.moveUp()
										if robot.getView()[0,2]:
											robot.moveUp()
											robot.moveDown()
											robot.moveUp()
											if robot.getView()[0,1]:
												robot.moveRight()
											else:
												robot.moveRight()
												if robot.getView()[0,2]:
													if robot.getView()[1,0]:
														robot.moveRight()
													else:
														robot.moveDown()
														if robot.getView()[1,2]:
															if robot.getView()[2,1]:
																if robot.getView()[2,1]:
																	robot.moveRight()
																else:
																	robot.moveLeft()
																	robot.moveUp()
															else:
																robot.moveUp()
														else:
															if robot.getView()[1,0]:
																robot.moveUp()
																robot.moveRight()
																robot.moveDown()
															else:
																pass
												else:
													if robot.getView()[0,2]:
														pass
													else:
														pass
										else:
											if robot.getView()[1,2]:
												if robot.getView()[1,2]:
													robot.moveRight()
													robot.moveUp()
												else:
													pass
											else:
												if robot.getView()[1,0]:
													robot.moveUp()
													if robot.getView()[1,0]:
														robot.moveUp()
														robot.moveUp()
														if robot.getView()[1,2]:
															robot.moveUp()
															robot.moveRight()
															robot.moveDown()
														else:
															robot.moveRight()
															if robot.getView()[1,2]:
																pass
															else:
																robot.moveLeft()
																robot.moveUp()
																robot.moveRight()
													else:
														pass
												else:
													robot.moveLeft()
													robot.moveLeft()
								else:
									robot.moveLeft()
	else:
		robot.moveDown()
		robot.moveDown()
		if robot.getView()[1,2]:
			if robot.getView()[2,1]:
				robot.moveRight()
			else:
				if robot.getView()[1,0]:
					robot.moveUp()
					robot.moveRight()
					robot.moveDown()
				else:
					pass
		else:
			if robot.getView()[1,2]:
				pass
			else:
				if robot.getView()[1,0]:
					robot.moveUp()
					robot.moveUp()
					if robot.getView()[0,2]:
						pass
					else:
						pass
				else:
					robot.moveLeft()