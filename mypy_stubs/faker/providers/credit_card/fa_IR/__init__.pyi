from .. import CreditCard as CreditCard, Provider as CreditCardProvider
from typing import Any

class Provider(CreditCardProvider):
    prefix_ansar: Any = ...
    prefix_iran_zamin: Any = ...
    prefix_hekmat: Any = ...
    prefix_keshavarzi: Any = ...
    prefix_shahr: Any = ...
    prefix_mehr_eghtesad: Any = ...
    prefix_sarmayeh: Any = ...
    prefix_post_bank: Any = ...
    prefix_tose: Any = ...
    prefix_eghtesad_novin: Any = ...
    prefix_meli: Any = ...
    prefix_pasargad: Any = ...
    prefix_tourism_bank: Any = ...
    prefix_ghavamin: Any = ...
    prefix_day: Any = ...
    prefix_mellat: Any = ...
    prefix_tejarat: Any = ...
    prefix_moasse_mellal: Any = ...
    prefix_saman_bank: Any = ...
    prefix_kosar: Any = ...
    prefix_refah: Any = ...
    prefix_saderat: Any = ...
    prefix_tat: Any = ...
    prefix_sina: Any = ...
    prefix_kar_afarin: Any = ...
    prefix_sepah: Any = ...
    prefix_maskan: Any = ...
    prefix_parsian: Any = ...
    prefix_bim: Any = ...
    credit_card_types: Any = ...
    def credit_card_expire(self, start: str = ..., end: str = ..., date_format: str = ...): ...
