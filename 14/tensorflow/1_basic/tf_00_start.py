﻿# -*- coding: utf-8 -*-

# TensorFlow
# Tensor : 임의의 차원을 갖는 배열들을 의미
# Google에서 2011년에 개발을 시작하여 
# 2015년에 오픈 소스로 공개한 기계학습 라이브러리

# 기존의 기계학습 라이브러리들에 비해서 
# 딥러닝과 기계학습 분야를 손쉽게 접근할 수 있도록 다양한 기능들을 제공
# (텐서보드와 같은 시각화 도구들이 자체적으로 제공됨)

# 장점
# 데이터 플로우 그래프를 통한 풍부한 표현력
# 계산 구조와 목표 함수만 정의하면 자동으로 미분 계산을 처리
# Python, C++, Go, Java, R 등의 대다수의 언어를 지원

# 텐서플로우 프로그래밍의 일반적인 순서
# 1. 기계학습을 실행하기 위해서 필요한 변수텐서(Tensor) 및 
#    연산텐서(Tensor)들을 정의
# 2. 각각의 변수텐서들을 연산텐서들을 사용하여 텐서플로우 그래프를 정의
# 3. 세션의 생성
# 4. 세션을 통한 그래프의 실행 및 수치 조정, 평가
# 5. 세션의 종료(프로그램 종료)

# 텐서플로우 모듈을 임포트
import tensorflow as tf

# 텐서의 정의(변수, 연산)
msg = tf.constant("Hello TensorFlow~!")
# 텐서의 내용을 출력(값이 출력되는 것이 아님)
# (텐서의 값을 출력하기 위해서는 세션을 통해서
# 가능함)
print(f"msg = {msg}")

# 텐서플로우를 실행하기 위한 세션 객체를 생성
# (세션이 생성되면서 텐서들을 구동시킬 준비)
sess = tf.Session()

# 세션 객체를 사용하여 텐서를 실행
# run 메소드는 매개변수로 전달된 텐서를 실행
# (변수인 경우 값을 반환, 연산인 경우 연산을 수헹)
result = sess.run(msg)
print(f"result = {result}")

# 세션을 종료
sess.close()
















