# Knight's Tour Game (Streamlit)

요청사항에 맞춰 기존 Tkinter 버전을 **Streamlit 배포용**으로 변경했습니다.

## 실행 방법

```bash
pip install streamlit
streamlit run knights_tour_game.py
```

## 배포 (Streamlit Community Cloud)

1. 이 저장소를 GitHub에 push
2. Streamlit Community Cloud에서 저장소 연결
3. Main file path를 `knights_tour_game.py`로 지정
4. Deploy

## 기능

- 보드 크기 선택: 6x6, 7x7, 8x8, 9x9, 10x10
- `Start New Game`으로 선택한 보드 크기 적용
- `Restart`로 현재 크기 보드 재시작
- 기사 이동 규칙(L자) 검증
- 중복 방문 방지
- 이동 수 / 남은 칸 / 현재 위치 표시
- 전체 칸 방문 시 완료 메시지 표시
