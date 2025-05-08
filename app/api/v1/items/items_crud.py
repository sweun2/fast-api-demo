from sqlalchemy.orm import Session
from app.core.models import Items as ItemsModel

class ItemsCrud:
    def __init__(self, db: Session):
        self.db = db
        
    def find_item_by_id(self, item_id: int) -> ItemsModel | None:
        return self.db.query(ItemsModel).filter(ItemsModel.id == item_id).first()
    def find_item_by_id_with_for_update(self, item_id: int) -> ItemsModel | None:
        return self.db.query(ItemsModel).filter(ItemsModel.id == item_id).with_for_update().first()
    
    def find_item_by_itemname(self, item_name: str) -> ItemsModel | None:
        return self.db.query(ItemsModel).filter(ItemsModel.itemname == item_name).first()

    def save_item(self, item: ItemsModel) -> ItemsModel:
        """
        아이템 저장 메서드
        Args:
            item (ItemsModel): 아이템 모델
        Returns:
            ItemsModel | None: 생성된 아이템 모델
        Commit: True
        """
        self.db.add(item)
        self.db.commit()
        self.db.refresh(item)
        return item
    
    def save_item_without_commit(self, item: ItemsModel) -> ItemsModel:
        """
        아이템 저장 메서드
        Args:
            item (ItemsModel): 아이템 모델
        Returns:
            ItemsModel | None: 생성된 아이템 모델
        Commit: True
        """
        self.db.add(item)
        self.db.flush()
        return item
    
    def delete_item(self, item: ItemsModel) -> None:
        """
        아이템 삭제 메서드
        Args:
            item (ItemsModel): 아이템 모델
        Returns:
            None
        Commit: True
        """
        self.db.delete(item)
        self.db.commit()