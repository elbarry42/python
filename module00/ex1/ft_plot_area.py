# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_plot_area.py                                    :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: elbarry <elbarry@student.42lyon.fr>        +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/01/28 18:20:19 by elbarry           #+#    #+#              #
#    Updated: 2026/01/29 11:59:59 by elbarry          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_plot_area() -> None :
    length = int(input("Enter length : "))
    width = int(input("Enter width : "))
    area = length * width
    print("Plot area : ", area)
