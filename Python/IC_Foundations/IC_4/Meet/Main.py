def sprawdz_wyniki(wyniki):
    zdajacy = 0

    for wynik in wyniki:
            czy_zdal = "zdał" if wynik > 60 else "nie zdał"
            print(f"{wynik} - {czy_zdal}")
            zdajacy += 1 if wynik > 60 else 0
    return zdajacy, zdajacy / len(wyniki) * 100, max(wyniki)

liczba, procent, najwiekszy = sprawdz_wyniki([72, 58, 90, 45, 88, 61, 100, 39, 77, 50])

print(f"liczba osób zdajacych: {liczba}")
print(f"procent osob zdajacych: {procent:.1f}")
print(f"najwyzszy wynik: {najwiekszy}")

